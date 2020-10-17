This folder contains the study results.

Each subfolder (ecg, text, audio, image) corresponds to each of the four studies.

Within each subfolder, a file "parse_XXX.py" will parse and generate the results for each study.

The "responses" or "round_X" folders contain the raw questionnaire responses.

Each response file includes the elapsed time of the response, the time of submission, and the questionnaire selections.

Each row includes a test index, and either (yes/no) for the validation question, or
	(method1, method2) indicating that the individual preferred the explanation
	of method1 over method2, for this particular test input.