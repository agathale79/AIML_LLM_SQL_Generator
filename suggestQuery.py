from google.cloud import aiplatform
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part



# Function that uses GenerativeModel API 
def generate(p_final_text):
    model = GenerativeModel("gemini-pro-vision")
    responses = model.generate_content(
        p_final_text,
    generation_config={
            "max_output_tokens": 2048,
            "temperature": 0.4,
            "top_p": 1,
            "top_k": 32
    },
    )
  
    print(responses.text)

# Initialize an empty list to store values
l_tabArr = []
l_tabColsArr = []


# Get the number of values to input
num_values = int(input("Enter the number of tables: "))

# Accept multiple values and store them in the array
for i in range(num_values):
    value = input(f"Enter Table {i + 1} Name: ")
    l_tabArr.append(value)
    colVal = input(f"Enter Table {i + 1} 's columns (comma seperated): ")
    l_tabColsArr.append(colVal)



tab_comma = ', '.join(l_tabArr)
l_tabColData=''
for i in range(len(l_tabColsArr)):
    l_tabColData=l_tabColData+l_tabArr[i]+': '+l_tabColsArr[i]+'\n'

print('Table Details::')
print(l_tabColData)

# Draft prompt 
l_sql=  input("What query do you want to generate? :: ")
l_final_text =  """Tables {0}. With comma separated fields mention below

{1}

{2}

"""
l_final_text=l_final_text.format(tab_comma,l_tabColData,l_sql)



#Call function
generate(l_final_text)