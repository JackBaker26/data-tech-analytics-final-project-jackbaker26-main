import pandas as pd
from bokeh.plotting import figure, show, output_file


df = pd.read_csv(r"C:\Users\Blazi\.vscode\data-tech-analytics-final-project-jackbaker26-main\target.csv", encoding="latin-1")
#print(df.duplicated().sum())
#print(df.isnull().sum().sum())
#print(len(df))
dl = pd.read_csv(r"C:\Users\Blazi\.vscode\data-tech-analytics-final-project-jackbaker26-main\Grocery Products Purchase.csv")
#dl = dl.drop_duplicates()
#print(dl.duplicated().sum())
#print(dl.isnull().sum().sum())
#print(len(dl))


ds = pd.read_csv(r"C:\Users\Blazi\.vscode\data-tech-analytics-final-project-jackbaker26-main\Supermart Grocery Sales - Retail Analytics Dataset.csv")
#ds = ds.drop_duplicates()
#print(ds.duplicated().sum())

# In this section i did some simple data cleaning and exploration. I checked for duplicates, missing values, and the length of the dataset. This is a crucial step in any data analysis project to ensure the quality and integrity of the data before proceeding with further analysis or modeling.


# this gave me some perspective that the first two datasets aern't sufficient for this project. The first dataset is too small and the second dataset is too messy. The third dataset is the most suitable for this project as it has a good amount of data and is relatively clean.
counts = ds['Region'].value_counts().reset_index()
counts.columns = ['Region', 'Count']
p = figure(
    x_range=counts['Region'].tolist(),
    x_axis_label='Region',
    y_axis_label='Count',
    width=800,
    height=400,
    tools="pan,wheel_zoom,box_zoom,reset,save"

)
p.vbar(x=counts['Region'], top=counts['Count'], width=0.9)

#output_file("region_counts.html")
#show(p)

counts2 = ds['Category'].value_counts().reset_index()   
counts2.columns = ['Category', 'Count']
p2 = figure(
    x_range=counts2['Category'].tolist(),
    x_axis_label='Category',
    y_axis_label='Count',
    width=800,
    height=400,
    tools="pan,wheel_zoom,box_zoom,reset,save"
)
p2.vbar(x=counts2['Category'], top=counts2['Count'], width=0.9)

#output_file("category_counts.html")
#show(p2)

counts3 = ds['City'].value_counts().reset_index()
counts3.columns = ['City', 'Count']
p3 = figure(
    x_range=counts3['City'].tolist(),
    x_axis_label='City',
    y_axis_label='Count',
    width=800,
    height=400,
    tools="pan,wheel_zoom,box_zoom,reset,save"
)
p3.vbar(x=counts3['City'], top=counts3['Count'], width=0.9)

#output_file("city_counts.html")
#show(p3)

counts4 = ds['Sub Category'].value_counts().reset_index()
counts4.columns = ['Sub Category', 'Count']
p4 = figure(
    x_range=counts4['Sub Category'].tolist(),
    x_axis_label='Sub Category',
    y_axis_label='Count',
    width=800,
    height=400,
    tools="pan,wheel_zoom,box_zoom,reset,save"
)
p4.vbar(x=counts4['Sub Category'], top=counts4['Count'], width=0.9)

output_file("sub_category_counts.html")
show(p4)



# Feedback given to me has highlighted that some of my datasets were bad. From past assignment troubles I've readjusted how i code these datasets and are a bit more proud of myself. I feel more confident in it and feel ive done better during this assignment. I think i will also need to improve some things and get more datasets in the future of this project.