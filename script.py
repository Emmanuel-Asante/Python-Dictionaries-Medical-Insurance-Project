# Add your code here
# Storing patient names and insurance costs

# Create an empty dictionary called medical_costs
medical_costs = {}

# Add some key-value pair to medical_costs
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0

# Add three key_value pairs to medical_costs
medical_costs.update({
  "Connie": 8886.0,
  "Isaac": 16444.0,
  "Valentina": 6420.0
})

# Display medical_costs
print(medical_costs)

# Update the value associated with Vinay to 3325.0
medical_costs["Vinay"] = 3325.0

# Display a new line
print("\n")

# Display the updated medical_costs data
print(medical_costs)

#  Create a variable called total_cost and set it equal to 0
total_cost = 0

# Iterate through the values in medical_costs and add each value to the total_cost variable
for value in medical_costs.values():
  total_cost += value

# Create a variable called average_cost that stores the total_cost divided by the length of the medical_costs dictionary
average_cost = total_cost / len(medical_costs)

# Display average_cost in an informative way
print("\nAverage Insurance Cost: {}".format(average_cost))

# List Comprehension to Dictionary

# Create a list called names that store's the names of patients
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]

# Create a list called ages that store's the ages of patients
ages = [27, 24, 43, 35, 52]

# Create a variable called zipped_ages that is a zipped list of pairs between the names list and the ages list
zipped_ages = zip(names, ages)

# Create a distionary called names_to_ages that iterates through zipped_ages and turns each pair into a key: value item
names_to_ages = {key: value for key, value in zipped_ages}

# Display a new line
print("\n")

# Print names_to_ages
print(names_to_ages)

# Store Marina's age in a variable called marina_age using the .get() method
marina_age = names_to_ages.get("Marina", None)

# Display marina_age
print("\nMarina's age is {}".format(marina_age))

# Using a Dictionary to create a medical database

# Create an empty dictionary called
medical_records = {}

# Add Marina's data to medical_records
medical_records["Marina"] = {
  "Age": 27,
  "Sex": "Female",
  "BMI": 31.1,
  "Children": 2,
  "Smoker": "Non-smoker",
  "Insurance_cost": 6607.0
  }

# Add Vinay's, Connie's, Isaac's and Valentina's data to medical_records
medical_records.update({
  "Vinay": {
    "Age": 24,
    "Sex": "Male",
    "BMI": 26.9,
    "Children": 0,
    "Smoker": "Non-smoker",
    "Insurance_cost": 3225.0
  },
  "Connie": {
    "Age": 43,
    "Sex": "Female",
    "BMI": 25.3,
    "Children": 3,
    "Smoker": "Non-smoker",
    "Insurance_cost": 8886.0
  },
  "Isaac": {
    "Age": 35,
    "Sex": "Male",
    "BMI": 20.6,
    "Children": 4,
    "Smoker": "Smoker",
    "Insurance_cost": 16444.0
  },
  "Valentina": {
    "Age": 52,
    "Sex": "Female",
    "BMI": 18.7,
    "Children": 1,
    "Smoker": "Non-smoker",
    "Insurance_cost": 6420.0
  }
})

# Display a new line
print("\n")

# Display medical_records
print(medical_records)

# Print out Connie's insurance cost
print("\nConnie's insurance cost is {} dollars.".format(medical_records["Connie"]["Insurance_cost"]))

# Remove Vinay from medical_records
medical_records.pop("Vinay")

# Iterate through the items of medical_records. For each key-value pair, print out the data from medical_records
for key, record in medical_records.items():
  print("\n" + key + " is a {} year old {} {} with a BMI of {} and insurance_cost of {}".format(record["Age"], record["Sex"], record["Smoker"], record["BMI"], record["Insurance_cost"]))

# Extra

# Create a function called update_medical_records() that takes in the name of an individual as well as their medical data
def update_medical_records(name, age, sex, smoker, bmi, insurance_cost):
  medical_data = {}
  medical_data[name] = {
    "Age": age,
    "Sex": sex,
    "Smoker": smoker,
    "BMI": bmi,
    "Insurance_cost": insurance_cost
  }
  return medical_records.update(medical_data)

# Update medical_records with Ruth's medical data
ruth_medical_data = update_medical_records(name = "Ruth", age = 23, sex = "Female", smoker = "Non-smoker", bmi = 18.5, insurance_cost = 2553.0)

# Update medical_records with Asaber's medical data
asaber_medical_data =  update_medical_records(name = "Asaber", age = 30, sex = "Male", smoker = "Non-smoker", bmi = 19.9, insurance_cost = 3985.0)

# Display a message
print("\nMedical Records, Ruth's and Asaber's medical data inclusive".upper())

# Display the updated medical_records data
for key, record in medical_records.items():
  print("\n" + key + " is a {} year old {} {} with a BMI of {} and insurance_cost of {}".format(record["Age"], record["Sex"], record["Smoker"], record["BMI"], record["Insurance_cost"]))

# Create a new dictionary
# Create an empty dictionary called countries_population_and_currencies
countries_population_and_currencies = {}

# Update countries_population_and_currencies with nine names of countries as keys and, their 2020 total populations and names of their currencies as values
countries_population_and_currencies.update({
  "Albania": {
    "Population": 2877797,
    "Currency": "Albanian Lek"
  },
  "Argentina": {
    "Population": 45195774,
    "Currency": "Argentine Peso"
  },
  "Armenia": {
    "Population": 2963243,
    "Currency": "Armenian Dram"
  },
  "Australia": {
    "Population": 25499884,
    "Currency": "Australian Dollar"
  },
  "Egypt": {
    "Population": 102334404,
    "Currency": "Egyptian Pound"
  },
  "Ghana": {
    "Population": 31072940,
    "Currency": "Ghana Cedi"
  },
  "Israel": {
    "Population": 8655535,
    "Currency": "Israel Shekel"
  },
  "Trinidad and Tobago": {
    "Population": 1399488,
    "Currency": "Trinidad and Tobago Dollar"
  },
  "United States": {
    "Population": 331002651,
    "Currency": "US Dollar"
  }

})

# Display countries_population_and_currencies
print("\n {}".format(countries_population_and_currencies))