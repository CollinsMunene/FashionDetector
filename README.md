# Fashion Detector
Hello there!! Have you ever imagined what if, instead of stressing yourself on what to where, you could just take a video of yourself and get a list of suggestions of what you can wear.<br>

<h3>Developers</h3><br>
<a href="https://github.com/CollinsMunene">Collins</a><br>

<h3>Tools</h3><br>
<ol>
    <li>IBM(visual recognition module)</li>
    <li>openCV</li>
    <li>python</li>
</ol>

<h2>TO NOTE:</h2>
Every project that constitutes anything AI or ML, it highly depends on the <b>model</b> used. For this project i'm still working on making it's model perfect(or close to).<br>

But it still works fine...<br>

And also i started with an assumption that the images i will be getting will be tops...hehehe

<b><i>The project is still IN PROGRESS. I will add more files, folders and information on the training and testing data used.
    If you are not familiar with IBM yet i highly suggest you check it out</i></b>
    

<h2>AIM OF THE PROJECT</h2><br>

The aim of this project is to allow one to take a video of themselves and the system should suggest what kind of clothes he/she could match well with.<br>


<h3>PROGRESS SO FAR</h3><br>

<b>For now we can handle to things:<br>
<ol>
    <li>As of now we are able to classify an uploaded image if it is a red or a blue top,(i started with training a model to identify if a top is either red or blue, so you can do more and better the model).<b>imagerecognition.py</b></li><br>
    <li>Also as for now you can take a video and concurrently the system will classify the images in the video if there is a red or blue top.<b>videorecognition.py</b></li><br>
</ol>
<h1>HOW DOES IT ACHIEVE THE TWO SO FAR</h1><br>

<p>For the first progress, the system is basic, we direct it to an existing image and it simply tells us based on our trained model, it identifies if the image has a red or blue top.</p><br><br>

<p>For the second progress, the system is average, we use openCV to capture a video stream then we break down the video stream into frames then into single images and save all that in the current directory, then we go through each and classify then using our model.</p><br><br>


We haven't yet achieved what we want, and the project is still in progress.<br>

<h1>GETTING STARTED</h1>
follow the following commands to get started and let's get this project to it's success

<ol>
<li>git clone https://github.com/CollinsMunene/FashionDetector.git</li>
<li>cd ClothDetector</li>
<li>source cloth_detector/bin/activate</li>
<li>Then run any of the .py files with python3 imagerecognition.py or python3 videorecognition.py</li>
</ol><br>

<h2>WHAT NEXT???</h2>
we have to make super changes to our model, to take it closer to perfection<br>

I am inviting YOU to take part on this project. If there is any question or comment don't hesitate to contact me at <br>

collinshillary1@gmail.com<br>
+254715804742<br>

<a href="https://collinsmunene.github.io/collinshillary.github.io/">Collins Portfolio</a><br>
We at <a href="https://collinsmunene.github.io/DevligenceLtd/">Devligence Ltd</a> are more than willing to work and listen to your amazing input and new ideas.





