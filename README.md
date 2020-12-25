# anime_face_generation

Contributors: Wentao Xu, Youyou Zhao, Roy Wang

The aim is to build a DCGAN (template from: https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html?highlight=dcgan) to generate high quality anime faces. 

We used danbooru.py to scrap our dataset from the Danbooru website. 

anime_haar.py (model from: http://ultraist.hatenablog.com/entry/20110718/1310965532) uses haar cascade method to detect and crop out the faces from the scraped data.

Location to the resources must be modified in dcgan.ipynb 

Run through the notebook to build the model. 
