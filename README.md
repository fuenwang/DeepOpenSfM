# DeepOpenSfM

## Intro
<p>
<a href="https://github.com/fuenwang/DeepOpenSfM">DeepOpenSfM</a> is additional python interface for 
<a href="https://github.com/mapillary/OpenSfM">OpenSfM</a>. Because the quality of 3D 
model reconstructed by <a href="https://github.com/mapillary/OpenSfM">OpenSfM</a> always depends on the quality of image matching, but traditional key-point-based matching methods usually get a lot of wrong correspondence. So we want to use deep learning to solve this tricky problem by making 
<a href="https://github.com/mapillary/OpenSfM">OpenSfM</a> support Deep-Learning-based matching method.For now we have already support 
<a href="http://lear.inrialpes.fr/src/deepmatching/">DeepMatching</a>, and we will continue to support 
more Deep-Learning-based matching method. Because the document is not completed yet, if you have any advise or question, just let us know!
</p>
<p align="center">
  <img src="demo_img/demo2.png"></img>
  <img src="demo_img/demo1.png"></img>
</p>

## Constrain
<p>
To make efficiency better, <a href="https://github.com/fuenwang/DeepOpenSfM">DeepOpenSfM</a> only supports sequential frames extracted 
from video; that is, you have to extract video into frames with same size and give theirs name in order like img0001.jpg, 
img0002.jpg....., and <a href="https://github.com/fuenwang/DeepOpenSfM">DeepOpenSfM</a> will do sequential matching like 
img0001.jpg---->img0002.jpg, img0001.jpg---->img0003.jpg, img0002.jpg---->img0003.jpg, img0002.jpg---->img0004.jpg and so on.
</p>
