import unittest
from pathlib import Path
import numpy as np
import os

# Assuming moviepy is installed in the environment for checks
# If not, these specific checks might need to be conditional or skipped
# In a real CI environment, moviepy would be a dev dependency
from unittest.mock import patch, MagicMock

# This flag is for the test file's direct use of moviepy, if any.
# The main code (tasks.py) now has its own MOVIEPY_AVAILABLE_TASKS flag.
try:
    from moviepy.editor import VideoFileClip 
    TEST_MOVIEPY_AVAILABLE = True
except ImportError:
    TEST_MOVIEPY_AVAILABLE = False
    VideoFileClip = None # Ensure it's defined for type hinting if not available

from PIL import Image # Added for creating test images

from geometor.seer.tasks.grid import Grid
# Import MOVIEPY_AVAILABLE_TASKS to know what the main code *thinks* it can do.
from geometor.seer.tasks.tasks import TaskPair, MOVIEPY_AVAILABLE_TASKS


class TestTaskPairVideo(unittest.TestCase):

    def setUp(self):
        self.test_files_to_clean = []
        # Ensure the 'videos' directory exists for test outputs
        self.video_output_dir = Path("test_videos")
        self.video_output_dir.mkdir(exist_ok=True)

    def tearDown(self):
        for file_path in self.test_files_to_clean:
            if file_path.exists():
                file_path.unlink()
        if self.video_output_dir.exists() and not any(self.video_output_dir.iterdir()):
             self.video_output_dir.rmdir()


    def _get_video_path(self, filename):
        return self.video_output_dir / filename

    def test_get_video_basic(self):
        input_grid_data = [[1, 0], [0, 1]]
        output_grid_data = [[0, 1], [1, 0]]
        task_pair = TaskPair("test_puzzle1", "train", 0, input_grid_data, output_grid_data)
        
        video_path = self._get_video_path("test_video_basic.mp4")
        self.test_files_to_clean.append(video_path)

        result_path = task_pair.get_video(output_path=str(video_path))
        if not MOVIEPY_AVAILABLE_TASKS:
            self.assertIsNone(result_path, "get_video should return None if moviepy is not available in tasks.py")
            self.assertFalse(video_path.is_file(), "Video file should not be created if moviepy is not available in tasks.py")
        else:
            # MOVIEPY_AVAILABLE_TASKS is True, so main code attempted video creation
            self.assertEqual(result_path, str(video_path))
            self.assertTrue(video_path.is_file())
            if TEST_MOVIEPY_AVAILABLE and VideoFileClip : # Check if moviepy is available for testing video content
                with VideoFileClip(str(video_path)) as clip:
                    self.assertEqual(clip.duration, 2.0) # 2 frames at 1 fps
            else:
                print("Skipping video content check in test_get_video_basic as moviepy.editor.VideoFileClip is not available in test environment.")

    def test_get_video_with_diff(self):
        input_grid_data = [[1, 0, 2], [0, 1, 0], [2, 2, 1]]
        output_grid_data = [[0, 1, 2], [1, 0, 0], [2, 1, 2]]
        task_pair = TaskPair("test_puzzle2", "train", 1, input_grid_data, output_grid_data)

        video_path = self._get_video_path("test_video_with_diff.mp4")
        self.test_files_to_clean.append(video_path)

        result_path = task_pair.get_video(output_path=str(video_path), include_diff_frame=True)
        if not MOVIEPY_AVAILABLE_TASKS:
            self.assertIsNone(result_path, "get_video should return None if moviepy is not available in tasks.py")
            self.assertFalse(video_path.is_file(), "Video file should not be created if moviepy is not available in tasks.py")
        else:
            self.assertEqual(result_path, str(video_path))
            self.assertTrue(video_path.is_file())
            if TEST_MOVIEPY_AVAILABLE and VideoFileClip:
                with VideoFileClip(str(video_path)) as clip:
                    self.assertEqual(clip.duration, 3.0) # Input, Diff, Output
            else:
                print("Skipping video content check in test_get_video_with_diff as moviepy.editor.VideoFileClip is not available in test environment.")

    def test_get_video_no_output(self):
        input_grid_data = [[1, 2], [3, 4]]
        task_pair = TaskPair("test_puzzle3", "test", 0, input_grid_data, output_grid=None)

        video_path = self._get_video_path("test_video_no_output.mp4")
        self.test_files_to_clean.append(video_path)

        result_path = task_pair.get_video(output_path=str(video_path))
        if not MOVIEPY_AVAILABLE_TASKS:
            self.assertIsNone(result_path, "get_video should return None if moviepy is not available in tasks.py")
            self.assertFalse(video_path.is_file(), "Video file should not be created if moviepy is not available in tasks.py")
        else:
            self.assertEqual(result_path, str(video_path))
            self.assertTrue(video_path.is_file())
            if TEST_MOVIEPY_AVAILABLE and VideoFileClip:
                with VideoFileClip(str(video_path)) as clip:
                    self.assertEqual(clip.duration, 1.0) # Only input frame
            else:
                print("Skipping video content check in test_get_video_no_output as moviepy.editor.VideoFileClip is not available in test environment.")

    def test_get_video_no_output_with_diff(self):
        """Test that include_diff_frame=True has no effect if there's no output."""
        input_grid_data = [[5, 6], [7, 8]]
        task_pair = TaskPair("test_puzzle4", "test", 1, input_grid_data, output_grid=None)

        video_path = self._get_video_path("test_video_no_output_with_diff.mp4")
        self.test_files_to_clean.append(video_path)

        # include_diff_frame is True, but should be ignored as no output exists
        result_path = task_pair.get_video(output_path=str(video_path), include_diff_frame=True)
        if not MOVIEPY_AVAILABLE_TASKS:
            self.assertIsNone(result_path, "get_video should return None if moviepy is not available in tasks.py")
            self.assertFalse(video_path.is_file(), "Video file should not be created if moviepy is not available in tasks.py")
        else:
            self.assertEqual(result_path, str(video_path))
            self.assertTrue(video_path.is_file())
            if TEST_MOVIEPY_AVAILABLE and VideoFileClip:
                with VideoFileClip(str(video_path)) as clip:
                    self.assertEqual(clip.duration, 1.0) # Still only input frame
            else:
                print("Skipping video content check in test_get_video_no_output_with_diff as moviepy.editor.VideoFileClip is not available in test environment.")

    # New tests using mocking
    @patch('geometor.seer.tasks.tasks.ImageSequenceClip')
    def test_get_video_frame_preparation_basic(self, mock_isc):
        if not MOVIEPY_AVAILABLE_TASKS:
            self.skipTest("Skipping frame preparation test as moviepy is marked unavailable in tasks.py")

        mock_clip_instance = MagicMock()
        mock_isc.return_value = mock_clip_instance

        input_grid_data = [[1]]
        output_grid_data = [[0]]
        task_pair = TaskPair("tp_mock1", "train", 0, input_grid_data, output_grid_data)
        
        video_path_str = str(self._get_video_path("mock_video_basic.mp4"))
        self.test_files_to_clean.append(Path(video_path_str))

        task_pair.get_video(output_path=video_path_str, include_diff_frame=False)

        mock_isc.assert_called_once()
        # Check the number of frames passed to ImageSequenceClip
        self.assertEqual(len(mock_isc.call_args[0][0]), 2) # Input + Output
        mock_clip_instance.write_videofile.assert_called_once_with(video_path_str, codec="libx264")

    @patch('geometor.seer.tasks.tasks.ImageSequenceClip')
    def test_get_video_frame_preparation_with_diff(self, mock_isc):
        if not MOVIEPY_AVAILABLE_TASKS:
            self.skipTest("Skipping frame preparation test as moviepy is marked unavailable in tasks.py")

        mock_clip_instance = MagicMock()
        mock_isc.return_value = mock_clip_instance

        input_grid_data = [[1,0], [0,1]]
        output_grid_data = [[0,1], [1,0]]
        task_pair = TaskPair("tp_mock2", "train", 1, input_grid_data, output_grid_data)
        
        video_path_str = str(self._get_video_path("mock_video_with_diff.mp4"))
        self.test_files_to_clean.append(Path(video_path_str))

        task_pair.get_video(output_path=video_path_str, include_diff_frame=True)

        mock_isc.assert_called_once()
        self.assertEqual(len(mock_isc.call_args[0][0]), 3) # Input + Diff + Output
        mock_clip_instance.write_videofile.assert_called_once_with(video_path_str, codec="libx264")

    @patch('geometor.seer.tasks.tasks.ImageSequenceClip')
    def test_get_video_frame_preparation_no_output(self, mock_isc):
        if not MOVIEPY_AVAILABLE_TASKS:
            self.skipTest("Skipping frame preparation test as moviepy is marked unavailable in tasks.py")
            
        mock_clip_instance = MagicMock()
        mock_isc.return_value = mock_clip_instance

        input_grid_data = [[1,2,3]]
        task_pair = TaskPair("tp_mock3", "test", 0, input_grid_data, output_grid=None)
        
        video_path_str = str(self._get_video_path("mock_video_no_output.mp4"))
        self.test_files_to_clean.append(Path(video_path_str))

        task_pair.get_video(output_path=video_path_str, include_diff_frame=False)
        mock_isc.assert_called_once()
        self.assertEqual(len(mock_isc.call_args[0][0]), 1) # Only Input
        mock_clip_instance.write_videofile.assert_called_once_with(video_path_str, codec="libx264")

    @patch('geometor.seer.tasks.tasks.ImageSequenceClip')
    def test_get_video_frame_preparation_no_output_with_diff(self, mock_isc):
        if not MOVIEPY_AVAILABLE_TASKS:
            self.skipTest("Skipping frame preparation test as moviepy is marked unavailable in tasks.py")

        mock_clip_instance = MagicMock()
        mock_isc.return_value = mock_clip_instance
        
        input_grid_data = [[4,5]]
        task_pair = TaskPair("tp_mock4", "test", 1, input_grid_data, output_grid=None)

        video_path_str = str(self._get_video_path("mock_video_no_output_with_diff.mp4"))
        self.test_files_to_clean.append(Path(video_path_str))

        task_pair.get_video(output_path=video_path_str, include_diff_frame=True)
        mock_isc.assert_called_once()
        self.assertEqual(len(mock_isc.call_args[0][0]), 1) # Only Input, diff frame is skipped
        mock_clip_instance.write_videofile.assert_called_once_with(video_path_str, codec="libx264")

    # --- Tests for new get_video functionality (actual_output_grid_pil provided) ---

    @patch('geometor.seer.tasks.tasks.TaskPair._generate_diff_image')
    @patch('geometor.seer.tasks.tasks.ImageSequenceClip')
    def test_gvideo_prep_actual_expected_no_diff(self, mock_isc, mock_gen_diff):
        if not MOVIEPY_AVAILABLE_TASKS:
            self.skipTest("Skipping: moviepy not available in tasks.py")
        
        mock_clip_instance = MagicMock()
        mock_isc.return_value = mock_clip_instance

        input_grid_data = [[1]]
        task_pair = TaskPair("tp_new1", "train", 0, input_grid_data, output_grid=None) # self.output not used here
        
        actual_pil = Image.new("RGB", (2,2), "blue")
        expected_pil = Image.new("RGB", (2,2), "red")
        
        video_path_str = str(self._get_video_path("mock_video_actual_expected_no_diff.mp4"))
        self.test_files_to_clean.append(Path(video_path_str))

        task_pair.get_video(output_path=video_path_str, include_diff_frame=False,
                            actual_output_grid_pil=actual_pil, expected_output_grid_pil=expected_pil)

        mock_isc.assert_called_once()
        args, _ = mock_isc.call_args
        self.assertEqual(len(args[0]), 3) # Input, Actual, Expected
        # Detailed check of frames:
        # args[0][0] is input_pil_np
        # args[0][1] is actual_pil_np
        # args[0][2] is expected_pil_np
        self.assertTrue(np.array_equal(args[0][1], np.array(actual_pil)))
        self.assertTrue(np.array_equal(args[0][2], np.array(expected_pil)))
        
        mock_gen_diff.assert_not_called() # Diff frame was not requested
        mock_clip_instance.write_videofile.assert_called_once_with(video_path_str, codec="libx264")

    @patch('geometor.seer.tasks.tasks.TaskPair._generate_diff_image')
    @patch('geometor.seer.tasks.tasks.ImageSequenceClip')
    def test_gvideo_prep_actual_expected_with_diff(self, mock_isc, mock_gen_diff):
        if not MOVIEPY_AVAILABLE_TASKS:
            self.skipTest("Skipping: moviepy not available in tasks.py")

        mock_clip_instance = MagicMock()
        mock_isc.return_value = mock_clip_instance
        mock_diff_pil = Image.new("RGB", (2,2), "yellow")
        mock_gen_diff.return_value = mock_diff_pil

        input_grid_data = [[1]]
        task_pair = TaskPair("tp_new2", "train", 0, input_grid_data, output_grid=None)
        
        actual_pil = Image.new("RGB", (2,2), "blue")
        expected_pil = Image.new("RGB", (2,2), "red")
        
        video_path_str = str(self._get_video_path("mock_video_actual_expected_with_diff.mp4"))
        self.test_files_to_clean.append(Path(video_path_str))

        task_pair.get_video(output_path=video_path_str, include_diff_frame=True,
                            actual_output_grid_pil=actual_pil, expected_output_grid_pil=expected_pil)

        mock_isc.assert_called_once()
        args, _ = mock_isc.call_args
        self.assertEqual(len(args[0]), 4) # Input, Actual, Diff, Expected
        self.assertTrue(np.array_equal(args[0][1], np.array(actual_pil)))
        self.assertTrue(np.array_equal(args[0][2], np.array(mock_diff_pil))) # Diff frame
        self.assertTrue(np.array_equal(args[0][3], np.array(expected_pil)))

        mock_gen_diff.assert_called_once_with(actual_pil, expected_pil)
        mock_clip_instance.write_videofile.assert_called_once_with(video_path_str, codec="libx264")

    @patch('geometor.seer.tasks.tasks.TaskPair._generate_diff_image')
    @patch('geometor.seer.tasks.tasks.ImageSequenceClip')
    def test_gvideo_prep_actual_no_expected_no_diff(self, mock_isc, mock_gen_diff):
        if not MOVIEPY_AVAILABLE_TASKS:
            self.skipTest("Skipping: moviepy not available in tasks.py")

        mock_clip_instance = MagicMock()
        mock_isc.return_value = mock_clip_instance

        input_grid_data = [[1]]
        task_pair = TaskPair("tp_new3", "train", 0, input_grid_data, output_grid=None)
        actual_pil = Image.new("RGB", (2,2), "blue")
        
        video_path_str = str(self._get_video_path("mock_video_actual_no_expected_no_diff.mp4"))
        self.test_files_to_clean.append(Path(video_path_str))

        task_pair.get_video(output_path=video_path_str, include_diff_frame=False,
                            actual_output_grid_pil=actual_pil, expected_output_grid_pil=None)
        
        mock_isc.assert_called_once()
        args, _ = mock_isc.call_args
        self.assertEqual(len(args[0]), 2) # Input, Actual
        self.assertTrue(np.array_equal(args[0][1], np.array(actual_pil)))
        
        mock_gen_diff.assert_not_called()
        mock_clip_instance.write_videofile.assert_called_once_with(video_path_str, codec="libx264")

    @patch('geometor.seer.tasks.tasks.TaskPair._generate_diff_image')
    @patch('geometor.seer.tasks.tasks.ImageSequenceClip')
    def test_gvideo_prep_actual_no_expected_with_diff(self, mock_isc, mock_gen_diff):
        if not MOVIEPY_AVAILABLE_TASKS:
            self.skipTest("Skipping: moviepy not available in tasks.py")

        mock_clip_instance = MagicMock()
        mock_isc.return_value = mock_clip_instance

        input_grid_data = [[1]]
        task_pair = TaskPair("tp_new4", "train", 0, input_grid_data, output_grid=None)
        actual_pil = Image.new("RGB", (2,2), "blue")

        video_path_str = str(self._get_video_path("mock_video_actual_no_expected_with_diff.mp4"))
        self.test_files_to_clean.append(Path(video_path_str))
        
        task_pair.get_video(output_path=video_path_str, include_diff_frame=True,
                            actual_output_grid_pil=actual_pil, expected_output_grid_pil=None)

        mock_isc.assert_called_once()
        args, _ = mock_isc.call_args
        self.assertEqual(len(args[0]), 2) # Input, Actual
        self.assertTrue(np.array_equal(args[0][1], np.array(actual_pil)))

        # _generate_diff_image should not be called if expected_output_grid_pil is None
        mock_gen_diff.assert_not_called()
        mock_clip_instance.write_videofile.assert_called_once_with(video_path_str, codec="libx264")


if __name__ == "__main__":
    unittest.main()


# --- Colors used by _generate_diff_image for assertions ---
# These are defined as np.array in the method, but we'll use tuples for PIL.getpixel()
ADDED_COLOR_T = (0, 255, 0)  # Green
REMOVED_COLOR_T = (255, 0, 0)  # Red
CHANGED_COLOR_T = (255, 255, 0)  # Yellow
SAME_COLOR_T = (192, 192, 192)  # Light Grey
BACKGROUND_COLOR_T = (0, 0, 0) # Black


class TestGenerateDiffImage(unittest.TestCase):

    def _create_pil_from_rgb_list(self, rgb_list_of_lists):
        """Creates a PIL image from a 2D list of RGB tuples."""
        height = len(rgb_list_of_lists)
        width = len(rgb_list_of_lists[0])
        img = Image.new("RGB", (width, height))
        pixels = img.load()
        for r in range(height):
            for c in range(width):
                pixels[c, r] = rgb_list_of_lists[r][c]
        return img

    def test_diff_none_images(self):
        img1 = self._create_pil_from_rgb_list([[(255,0,0)]])
        self.assertIsNone(TaskPair._generate_diff_image(None, img1))
        self.assertIsNone(TaskPair._generate_diff_image(img1, None))
        self.assertIsNone(TaskPair._generate_diff_image(None, None))

    def test_diff_identical_images(self):
        img_data = [[(10, 20, 30), (40, 50, 60)], [(70, 80, 90), (100, 110, 120)]]
        img1 = self._create_pil_from_rgb_list(img_data)
        img2 = self._create_pil_from_rgb_list(img_data)
        
        diff_img = TaskPair._generate_diff_image(img1, img2)
        self.assertIsNotNone(diff_img)
        self.assertEqual(diff_img.size, (2, 2))
        for r in range(2):
            for c in range(2):
                self.assertEqual(diff_img.getpixel((c, r)), SAME_COLOR_T)

    def test_diff_completely_different_images_same_size(self):
        img1_data = [[(10, 20, 30)]]
        img2_data = [[(40, 50, 60)]]
        img1 = self._create_pil_from_rgb_list(img1_data)
        img2 = self._create_pil_from_rgb_list(img2_data)

        diff_img = TaskPair._generate_diff_image(img1, img2)
        self.assertEqual(diff_img.getpixel((0,0)), CHANGED_COLOR_T)

    def test_diff_image1_larger(self):
        # img1: 2x1, img2: 1x1
        img1_data = [[(10,10,10), (255,0,0)]] # Second pixel is 'removed'
        img2_data = [[(10,10,10)]]
        img1 = self._create_pil_from_rgb_list(img1_data)
        img2 = self._create_pil_from_rgb_list(img2_data)

        diff_img = TaskPair._generate_diff_image(img1, img2)
        self.assertEqual(diff_img.size, (2,1))
        self.assertEqual(diff_img.getpixel((0,0)), SAME_COLOR_T)
        self.assertEqual(diff_img.getpixel((1,0)), REMOVED_COLOR_T)

    def test_diff_image2_larger(self):
        # img1: 1x1, img2: 2x1
        img1_data = [[(10,10,10)]]
        img2_data = [[(10,10,10), (0,255,0)]] # Second pixel is 'added'
        img1 = self._create_pil_from_rgb_list(img1_data)
        img2 = self._create_pil_from_rgb_list(img2_data)

        diff_img = TaskPair._generate_diff_image(img1, img2)
        self.assertEqual(diff_img.size, (2,1))
        self.assertEqual(diff_img.getpixel((0,0)), SAME_COLOR_T)
        self.assertEqual(diff_img.getpixel((1,0)), ADDED_COLOR_T)

    def test_diff_mixed_changes(self):
        # img1: 2x2
        # S C
        # R B (B = background, effectively removed from img1's perspective if img2 is smaller)
        img1_data = [
            [(1,1,1), (2,2,2)], # Same, Changed
            [(3,3,3), (4,4,4)]  # Removed, Removed (this one becomes background in a 2x1 img2)
        ]
        # img2: 2x1 (effectively, second row of img1 is 'removed')
        # S A (A = added, where img1 had (2,2,2) but img2 has (5,5,5) and also extends)
        # (effectively, img1 had (3,3,3) and (4,4,4) in row 2, img2 has nothing)
        img2_data = [ # 2x2 for direct comparison, then test with 2x1
            [(1,1,1), (5,5,5)], # Same, Changed (was 2,2,2 now 5,5,5)
            [(6,6,6), (7,7,7)]  # Added, Added
        ]
        img1 = self._create_pil_from_rgb_list(img1_data) # 2x2
        img2 = self._create_pil_from_rgb_list(img2_data) # 2x2 for this test case

        # Expected diff for 2x2 comparison:
        # SAME    CHANGED
        # CHANGED CHANGED (since (3,3,3) became (6,6,6) and (4,4,4) became (7,7,7))
        # Let's adjust img2_data to make it more interesting:
        # img1_data:
        # A B
        # C D
        # img2_data:
        # A E  (A is same, B->E is changed)
        # F G  (C->F is changed, D->G is changed)
        
        img1_data_complex = [
            [(10,10,10), (20,20,20)], # Pixel A, Pixel B
            [(30,30,30), (40,40,40)]  # Pixel C, Pixel D
        ]
        img2_data_complex = [
            [(10,10,10), (25,25,25)], # Pixel A (Same), Pixel E (Changed from B)
            [(35,35,35), (40,40,40)]  # Pixel F (Changed from C), Pixel D (Same as D if we make it same)
        ]
        img1 = self._create_pil_from_rgb_list(img1_data_complex)
        img2 = self._create_pil_from_rgb_list(img2_data_complex)

        diff_img = TaskPair._generate_diff_image(img1, img2)
        self.assertEqual(diff_img.size, (2,2))
        self.assertEqual(diff_img.getpixel((0,0)), SAME_COLOR_T)    # A vs A
        self.assertEqual(diff_img.getpixel((1,0)), CHANGED_COLOR_T) # B vs E
        self.assertEqual(diff_img.getpixel((0,1)), CHANGED_COLOR_T) # C vs F
        # Let's make D in img2_data_complex same as D in img1_data_complex for clarity
        img2_data_complex[1][1] = (40,40,40)
        img2 = self._create_pil_from_rgb_list(img2_data_complex)
        diff_img = TaskPair._generate_diff_image(img1, img2)
        self.assertEqual(diff_img.getpixel((1,1)), SAME_COLOR_T) # D vs D (now same)

    def test_diff_image_content_vs_background(self):
        # img1 is 1x1, img2 is 2x1. img1's content is where img2 has background.
        img1_data = [[(10,10,10)]]
        img2_data = [[(0,0,0), (20,20,20)]] # img2's (0,0) is black, matches BACKGROUND_COLOR
        img1 = self._create_pil_from_rgb_list(img1_data)
        img2 = self._create_pil_from_rgb_list(img2_data)
        
        # array1[0,0] = (10,10,10)
        # array2[0,0] = (0,0,0) -> this is background, so effectively img1 has content where img2 has background
        # This means pixel (0,0) in img1 is REMOVED relative to img2 (if we consider img2 as the 'base' + additions)
        # or CHANGED if we consider (0,0,0) as a valid color in img2.
        # The logic is:
        # if in_img2 and not in_img1: ADDED
        # elif in_img1 and not in_img2: REMOVED
        # elif in_img1 and in_img2: compare pixels
        #
        # (0,0): in_img1=T, in_img2=T. array1[0,0]=(10,10,10), array2[0,0]=(0,0,0). Result: CHANGED
        # (1,0): in_img1=F, in_img2=T. array2[1,0]=(20,20,20). Result: ADDED

        diff_img = TaskPair._generate_diff_image(img1, img2)
        self.assertEqual(diff_img.size, (2,1))
        self.assertEqual(diff_img.getpixel((0,0)), CHANGED_COLOR_T)
        self.assertEqual(diff_img.getpixel((1,0)), ADDED_COLOR_T)
