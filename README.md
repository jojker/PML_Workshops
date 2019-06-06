# Physics Machine Learning Club Summer Workshop TO-DO list

This is where the Physics Machine Learning Club puts its workshop materials. We are creating an ambitious new workshop for the summer of 2019. 
**We have reserved Cupples I room 115 for 10 AM to 3 PM on every Tue/Thu from July 30-Aug 16.** (There is construction in Crow Hall) 
If we (as a group) re-write one notebook a day we will be done in time for the workshop. As of 06/06 there are 54 days and 49 un-finished examples. If everyone does just a handful then we'll be done way sooner.

Currently we have gathered material and are working to transcribe new workshop materials from old materials, or from resources we found online. A number of people have offered to volunteer to curate one or more workshops. If you're reading this, then hopefully you are one of them!

## Here is what you need to know and need to do.
### general details
1. The Workshops are organized into 6 days; we booked the room for 4 hours. Each will consist of a series of walk-throughs of worked examples. The walk-throughs should last between 10 and 30 minutes. 
2. Repository Structure: The folder "Summer 2019" is organized like so: ![Image of folder tree](https://github.com/jojker/PML_Workshops/blob/master/Summer%202019.png)  Each sub-folder beginning with "Ex # - " is named after the task which we *think* we need to provide an example of. However, its only approximate. **If you have a related (or more interesting) task and decide to provide an example feel free to change the name of the example sub-folder**. In each example sub-folder there is a collection of weblinks and/or folders. These folders contain old workshops that can be adapted in whole or in part to fit the intended example. The weblinks usually link to example code. Sometimes the link points to a complete Jupyter notebook that could be taken as is or modified only a little (e.g. replacing technical background with hints at how to adapt the code). 
3. **The final format for the example subfolder contents should be:** One video file (mp4) containing a recording of a walk-through of the notebook (may be recorded after the workshop, doesn't have to be the exact same notebook). one-three Jupyter notebooks (e.g. three 10-minute notebooks of closely related examples). A sub-folder called "Data" will usually also be there, it contains the data needed to run the examples. There may be a sub-folder called "additional resources" that contains links to anything we think might be helpful. There may also be another folder called "slides" *IF* the video included extra slides, the walk-through should not have slides but should have all images and content in the comments of the Jupyter notebook itself.
4. Start picking subfolders and creating/choosing Jupyter notebooks. **The notebooks should be focused on showing how attendees can adapt what they see to their own work.** We DO NOT want lengthy explanations of "auto-grad" or neural architecture. Brief mentions are OK, linking to explanations for attendees to view on their own time is great. Please make sure that you emphasize the actions audience members can take to adapt the code. This means making comments that say: "Redirect this link to a folder of images to one of your own folders" or "You'll need to replace this Pandas code with code that extract your data from however you stored it."
5. Attendees will have backgrounds that are all over the place. Some will find it hard to follow a sequence of commands in an object-oriented language or dynamic programming example, some will only deal with math in coursework. This is related to #3 above: DONT include many technical details about the linear algebra, calculus, and statistical assumptions underlying the algorithm, **it is more helpful to explain how to "read the code"**. In otherwords the most valuable background is the "logic" behind why each python library's commands are written in a certain way. For example: "The matrix object has an action it can perform call transpose so we use 'mat.transpose()'." This is especially true for people comming from a Matlab background because there is little to no OOP or Dynamic Programming in typical Matlab use cases. Most attendees will have written 500 lines of code or less, few will have written over 10K. DO reference and link to details and admonish attendees to avoid *publishing* findings until they understand the linear algebra, calculus, and statistical assumptions.
6. **If you adapt someone else's code or notebook ALWAYS cite them loudly and clearly** and make sure you aren't violating a license. We are using it for educational purposes with no commercial gain. You can always use a notebook or code as-is (on the original website) but they probably have very different goals. 


### specific tasks
- James will begin making notebooks immediately, he will follow along with videos after 90% of the examples have completed notebooks. You are encouraged to make video walk-throughs yourself.
- Video walk-throughs: The simplest way is to record a Skype call to yourself with screen sharing on then edit it afterwards. If you like you can ask someone else to edit it. You might try ["ShotCut"](https://shotcut.org/) or ["DaVinci Resolve 15"](https://www.engadget.com/2018/08/22/davinci-resolve-15-free-hollywood-video-editor-review) as *possible* free video editing software. We should always be able to see your face and the video should not have clumsy transitions where you switch windows. Turn off screen sharing to show a larger image of your face when necessary (e.g. the intro). You can crop out the Skype junk, and trim out the transitions later.
- Curating a notebook. Do you have a Jupyter notebook that is a close match already? Do you know of one online? Drop the notebook (or a link to it) in the appropriate example folder (re name the folder if you want) and put your name in the file name so we can thank you. One of us will come along and suitably modify the materials.
- Creating a notebook. See the brief summary above. This is a great excuse to create training materials for your lab mates or to learn something new!
- Leading a walk-through. Pick a notebook and claim it. Put your name in the title of the notebook if no one else has. The person who made the notebook always has priority. When it comes time to present the notebook in the workshop, you'll be called up to guide the audience. This is a good excuse for you to familiarize yourself with something. 
- Helping by proctoring. Pick a few notebooks and open them in google colab. Make sure you know how to run them. If not email James for help. Then you can help attendees sort through their troubles during the workshops.
- Organizing the example folders. Currently they are just piles of resources. When a person creates the notebooks they may not carefully format them according to bullet 3. It should be pretty simple to just re-organize the folder and test the notebook to make sure nothing is broken.


### Examples ranked by how easy they will be to finish
1. Most easy - notebooks exist but need adaptation - 
Day 2: Ex 2, 3 - 
Day 4: Ex 2, 3, 4 -  
Day 5: Ex 2, 7 - 
Day 6: Ex 2, 3, 5, 7
2. Notebooks and Code examples exist but are not quite right, need to combine or add - 
Day 2: Ex 1, 4, 5, 7 - 
Day 3: Ex 4, 6 - 
Day 4: Ex 1, 6 - 
Day 5: Ex 3, 4 - 
Day 6: Ex 4
3. No notebooks/code or bad notebooks/code. Lots of helpful resources and it's not too hard to build from scratch - 
Day 1: Ex 2, 3, 6, 7 - 
Day 3: Ex 3 - 
Day 4: Ex 5, 7 - 
Day 6: Ex 1
4. A useful challenge! Bad notebooks/code or need to combine resources in creative ways to satisfy the example, or need to build from scratch from journal/magazine articles or forum posts and personal experience. - 
Day 1: Ex 1, 4, 5 - 
Day 2: Ex 6 - 
Day 3: Ex 1, 2, 7 - 
Day 5: Ex 1, 5, 6 - 
Day 6: Ex 6
