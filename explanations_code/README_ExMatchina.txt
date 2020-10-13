To use the ExMatchina library

1) import the ExMatchina class

2) load ExMatchina with a particular model + examples (training data)

training_data = np.load('./X_train.npy')
model = load_model('./model')
selected_layer = "Flatten_1"

exm = ExMatchina(model=model, layer=selected_layer, examples=training_data)

3) fetch examples and corresponding indices with 

test_data = np.load('./X_test.npy')
test_input = test_data[0]
(examples, indices) = exm.return_nearest_examples(test_input)

4) plot the examples in whatever manner is preferable