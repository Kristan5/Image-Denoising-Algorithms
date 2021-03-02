Dependencies:
- Numpy
- OpenCV
- Pillow
- Python 3.8.2

All algorithms can be found in in the 'FilteringAlgorithms' directory. 
In order to run any of them you can simply run:

```python ModeFilter.py``` or ```python3 ModeFilter.py```

The estimation of image noise variance metric/ algorithm can be found in 
the 'RankAlgorithm' directory and can be run in the same way as the other 
algorithms: 

```python Rank.py``` or ```python3 Rank.py```

This algorithm usually takes quite some time to complete execution simply
due to the nature of its design. To change the files its using, you can 
change the first line of main function containing the filepaths. 


