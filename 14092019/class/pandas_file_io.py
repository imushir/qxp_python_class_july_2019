import pandas as pd

file_path = "D:\\qxp_python_class_july_2019\\14092019\\class\\demo_file.csv"
out_put_csv = "D:\\qxp_python_class_july_2019\\14092019\\class\\marks.csv"

data_table = pd.read_csv(file_path)
print("Data table is\n", data_table)


'''
for each_row in data_table.iterrows():
    print("Each row is row ", each_row)
'''


# list of name, degree, score 
nme = ["aparna", "pankaj", "sudhir", "Geeku"] 
deg = ["MBA", "BCA", "M.Tech", "MBA"] 
scr = [90, 40, 80, 98] 
   
# dictionary  
student_details = {'name': nme, 'degree': deg, 'score': scr}  
     
student_table = pd.DataFrame(student_details) 
  
# saving the dataframe 
student_table.to_csv(out_put_csv, index=False)