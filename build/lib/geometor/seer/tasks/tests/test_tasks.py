import unittest
from pathlib import Path
import numpy as np
import os

# Assuming moviepy is installed in the environment for checks
# If not, these specific checks might need to be conditional or skipped
# In a real CI environment, moviepy would be a dev dependency
try:
    from moviepy.editor import VideoFileClip
    MOVIEPY_AVAILABLE = True
except ImportError:
    MOVIEPY_AVAILABLE = False

from geometor.seer.tasks.grid import Grid
from geometor.seer.tasks.tasks import TaskPair


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
        self.assertEqual(result_path, str(video_path))
        self.assertTrue(video_path.is_file())

        if MOVIEPY_AVAILABLE:
            with VideoFileClip(str(video_path)) as clip:
                self.assertEqual(clip.duration, 2.0) # 2 frames at 1 fps
                self.assertEqual(len(list(clip.iter_frames())), 2)

    def test_get_video_with_diff(self):
        input_grid_data = [[1, 0, 2], [0, 1, 0], [2, 2, 1]]
        output_grid_data = [[0, 1, 2], [1, 0, 0], [2, 1, 2]]
        task_pair = TaskPair("test_puzzle2", "train", 1, input_grid_data, output_grid_data)

        video_path = self._get_video_path("test_video_with_diff.mp4")
        self.test_files_to_clean.append(video_path)

        result_path = task_pair.get_video(output_path=str(video_path), include_diff_frame=True)
        self.assertEqual(result_path, str(video_path))
        self.assertTrue(video_path.is_file())

        if MOVIEPY_AVAILABLE:
            with VideoFileClip(str(video_path)) as clip:
                self.assertEqual(clip.duration, 3.0) # Input, Diff, Output
                self.assertEqual(len(list(clip.iter_frames())), 3)

    def test_get_video_no_output(self):
        input_grid_data = [[1, 2], [3, 4]]
        task_pair = TaskPair("test_puzzle3", "test", 0, input_grid_data, output_grid=None)

        video_path = self._get_video_path("test_video_no_output.mp4")
        self.test_files_to_clean.append(video_path)

        result_path = task_pair.get_video(output_path=str(video_path))
        self.assertEqual(result_path, str(video_path))
        self.assertTrue(video_path.is_file())

        if MOVIEPY_AVAILABLE:
            with VideoFileClip(str(video_path)) as clip:
                self.assertEqual(clip.duration, 1.0) # Only input frame
                self.assertEqual(len(list(clip.iter_frames())), 1)

    def test_get_video_no_output_with_diff(self):
        """Test that include_diff_frame=True has no effect if there's no output."""
        input_grid_data = [[5, 6], [7, 8]]
        task_pair = TaskPair("test_puzzle4", "test", 1, input_grid_data, output_grid=None)

        video_path = self._get_video_path("test_video_no_output_with_diff.mp4")
        self.test_files_to_clean.append(video_path)

        # include_diff_frame is True, but should be ignored as no output exists
        result_path = task_pair.get_video(output_path=str(video_path), include_diff_frame=True)
        self.assertEqual(result_path, str(video_path))
        self.assertTrue(video_path.is_file())

        if MOVIEPY_AVAILABLE:
            with VideoFileClip(str(video_path)) as clip:
                self.assertEqual(clip.duration, 1.0) # Still only input frame
                self.assertEqual(len(list(clip.iter_frames())), 1)

if __name__ == "__main__":
    unittest.main()
