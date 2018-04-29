from java_data import data



final = {}
final["data"] = []

for key in data:
	new = {}
	new["topic"] = key
	new["questions"] = []
	new["answers"] = []

	for qa in data[key]:
		if len(qa) != 2:
			continue
		new["questions"].append(qa[0])
		new["answers"].append(qa[1])
	final["data"].append(new)

print(final)
