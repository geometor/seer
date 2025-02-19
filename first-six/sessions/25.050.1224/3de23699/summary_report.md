┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                        Task Summary                                        ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                            Task Responses                            
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━┳━━━━━━━━━━┓
┃ file              ┃ prompt ┃ candidate ┃ cached ┃ total ┃ Time (s) ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━╇━━━━━━━━━━┩
│ 001-response.json │   1589 │       630 │      0 │  2219 │   9.4999 │
│ 002-response.json │   2308 │       253 │      0 │  2561 │  40.8961 │
│ 003-response.json │   3256 │      1160 │      0 │  4416 │  14.4446 │
│ 004-response.json │   4504 │       253 │      0 │  4757 │   3.2027 │
│ 005-response.json │   5574 │      1159 │      0 │  6733 │  12.5632 │
│ 006-response.json │   6821 │       423 │      0 │  7244 │   4.4531 │
│ 007-response.json │   8189 │      1118 │      0 │  9307 │  12.2758 │
│ 008-response.json │   9396 │       431 │      0 │  9827 │   4.7488 │
│ TOTAL             │  41637 │      5427 │      0 │ 47064 │ 102.0843 │
└───────────────────┴────────┴───────────┴────────┴───────┴──────────┘
                                        Code File: 002                                        
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Example ┃ Status                              ┃ size ┃ palette ┃ color count ┃ diff pixels ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ 1       │ FAILED                              │ ✅   │ ✅      │ ❌          │ 1           │
│ 2       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (3,3) (3,5)                         │      │         │             │             │
│ 3       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (3,3) (4,4)                         │      │         │             │             │
│ 4       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (3,3) (4,8)                         │      │         │             │             │
└─────────┴─────────────────────────────────────┴──────┴─────────┴─────────────┴─────────────┘
                                        Code File: 003                                        
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Example ┃ Status                              ┃ size ┃ palette ┃ color count ┃ diff pixels ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ 1       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (3,5) (3,3)                         │      │         │             │             │
│ 2       │ FAILED                              │ ✅   │ ✅      │ ❌          │ 5           │
│ 3       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (3,5) (4,4)                         │      │         │             │             │
│ 4       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (3,5) (4,8)                         │      │         │             │             │
└─────────┴─────────────────────────────────────┴──────┴─────────┴─────────────┴─────────────┘
                                        Code File: 004                                        
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Example ┃ Status                              ┃ size ┃ palette ┃ color count ┃ diff pixels ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ 1       │ FAILED                              │ ✅   │ ✅      │ ❌          │ 1           │
│ 2       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (3,3) (3,5)                         │      │         │             │             │
│ 3       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (3,3) (4,4)                         │      │         │             │             │
│ 4       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (3,3) (4,8)                         │      │         │             │             │
└─────────┴─────────────────────────────────────┴──────┴─────────┴─────────────┴─────────────┘
                                        Code File: 005                                        
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Example ┃ Status                              ┃ size ┃ palette ┃ color count ┃ diff pixels ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ 1       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (4,4) (3,3)                         │      │         │             │             │
│ 2       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (4,4) (3,5)                         │      │         │             │             │
│ 3       │ FAILED                              │ ✅   │ ✅      │ ❌          │ 4           │
│ 4       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (4,4) (4,8)                         │      │         │             │             │
└─────────┴─────────────────────────────────────┴──────┴─────────┴─────────────┴─────────────┘
                                        Code File: 006                                        
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Example ┃ Status                              ┃ size ┃ palette ┃ color count ┃ diff pixels ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ 1       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (4,4) (3,3)                         │      │         │             │             │
│ 2       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (4,4) (3,5)                         │      │         │             │             │
│ 3       │ FAILED                              │ ✅   │ ✅      │ ❌          │ 4           │
│ 4       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (4,4) (4,8)                         │      │         │             │             │
└─────────┴─────────────────────────────────────┴──────┴─────────┴─────────────┴─────────────┘
                                        Code File: 007                                        
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Example ┃ Status                              ┃ size ┃ palette ┃ color count ┃ diff pixels ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ 1       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (4,8) (3,3)                         │      │         │             │             │
│ 2       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (4,8) (3,5)                         │      │         │             │             │
│ 3       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (4,8) (4,4)                         │      │         │             │             │
│ 4       │ FAILED                              │ ✅   │ ✅      │ ❌          │ 6           │
└─────────┴─────────────────────────────────────┴──────┴─────────┴─────────────┴─────────────┘
                                        Code File: 008                                        
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Example ┃ Status                              ┃ size ┃ palette ┃ color count ┃ diff pixels ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ 1       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (4,8) (3,3)                         │      │         │             │             │
│ 2       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (4,8) (3,5)                         │      │         │             │             │
│ 3       │ ERROR: operands could not be        │ ❌   │ ❌      │ ❌          │ N/A         │
│         │ broadcast together with shapes      │      │         │             │             │
│         │ (4,8) (4,4)                         │      │         │             │             │
│ 4       │ FAILED                              │ ✅   │ ✅      │ ❌          │ 6           │
└─────────┴─────────────────────────────────────┴──────┴─────────┴─────────────┴─────────────┘
