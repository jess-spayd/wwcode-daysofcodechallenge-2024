## Questionnaire
1. Do you need these for deep learning?
   - Lots of math T / **F**
   - Lots of data T / **F**
   - Lots of expensive computers T / **F**
   - A PhD T / **F**
2. Name five areas where deep learning is now the best in the world.
    - NLP
    - computer vision
    - recommendation systems
    - image generation
    - games
3. What was the name of the first device that was based on the principle of the artificial neuron?
    - Mark I Perceptron
4. Based on the book of the same name, what are the requirements for parallel distributed processing (PDP)?
    - A set of processing units
    - A state of activation
    - An output function for each unit
    - A pattern of connectivity among units
    - A propagation rule for propagating patterns of activities through the network of connectivities
    - An activation rule for combining the inputs impinging on a unit with the current state of that unit to produce an output for the unit
    - A learning rule whereby patterns of connectivity are modified by experience
    - An environment within which the system must operate
5. What were the two theoretical misunderstandings that held back the field of neural networks?
    - 
    - 
6. What is a GPU?
    - A special kind of processor in your computer that can handle thousands of single tasks at the same time
7. Open a notebook and execute a cell containing: `1+1`. What happens?
    - It add 1+1 and returns 2.
8. Follow through each cell of the stripped version of the notebook for this chapter. Before executing each cell, guess what will happen.
9. Complete the Jupyter Notebook online appendix.
10. Why is it hard to use a traditional computer program to recognize images in a photo?
    - Traditional programs require you to list steps, but the steps in recognize an image are hard to define.
11. What did Samuel mean by "weight assignment"?
    - Weight assignments are values that define how the program will operate.
12. What term do we normally use in deep learning for what Samuel called "weights"?
    - parameters
13. Draw a picture that summarizes Samuel's view of a machine learning model.
14. Why is it hard to understand why a deep learning model makes a particular prediction?
15. What is the name of the theorem that shows that a neural network can solve any mathematical problem to any level of accuracy?
    - Universal approximation theorem
16. What do you need in order to train a model?
    - data with labels
17. How could a feedback loop impact the rollout of a predictive policing model?
    - It can reinforce bias by predicting arrests rather than crime.
18. Do we always have to use 224×224-pixel images with the cat recognition model?
    - No. Larger pictures will produce better models but at the cost of speed and memory.
19. What is the difference between classification and regression?
    - Classification predicts categories; regression predicts numeric values.
20. What is a validation set? What is a test set? Why do we need them?
    - The validation set is a chunk of the data used to evaluate how well the model works. This can be used to continue tuning the model. The test set is only used at the very end to show the efficacy of the model once it has been fine-tuned.
21. What will fastai do if you don't provide a validation set?
    - It will create one for you.
22. Can we always use a random sample for a validation set? Why or why not?
    - It should be random but with a seed set so that every time you make changes to the model, the results will be directly comparable, as opposed to a new random sample every time.
23. What is overfitting? Provide an example.
    - A model overfits if it predicts the validation set very well but performs poorly on new data.
24. What is a metric? How does it differ from "loss"?
    - Metrics measure the quality of the model's predictions. Loss is information for the model to use in training. Metrics are for humans to understand the model's efficacy.
25. How can pretrained models help?
    - Pretrained models are already tuned to the type of data and can already do some work. They will require tuning.
26. What is the "head" of a model?
    - The last layer of a model which will be customized to the specific training task.
27. What kinds of features do the early layers of a CNN find? How about the later layers?
    - The layers progressively find more refined characteristics.
28. Are image models only useful for photos?
    - No, they can be used with other kinds of data.
29. What is an "architecture"?
    - The functional form of a model (type of model)
30. What is segmentation?
    - When a model can recognize every pixel of an image.
31. What is `y_range` used for? When do we need it?
    - `y_range` gives the scale/range of the value we are predicting. This is needed when predicting a continuous value.
32. What are "hyperparameters"?
    - "Parameters about parameters:" making choices to adjust the model.
33. What's the best way to avoid failures when using AI in an organization?
    - using validation and test sets

## Further Research
1. Why is a GPU useful for deep learning? How is a CPU different, and why is it less effective for deep learning?
2. Try to think of three areas where feedback loops might impact the use of machine learning. See if you can find documented examples of that happening in practice.