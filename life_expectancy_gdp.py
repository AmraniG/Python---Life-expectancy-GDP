#For this project, you will analyze data on GDP and life expectancy from the World Health Organization and the World Bank to try and identify the relationship 
# between the GDP and life expectancy of six countries.
# During this project, you will analyze, prepare, and plot data in order to answer questions in a meaningful way.
# After you perform your analysis, you’ll be creating a blog post to share your findings on the World Health Organization website.


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_to_import = 'C:\\Users\\Ghisl\\OneDrive\\Documents\\Formations\\Python\\GDP Expectancy\\all_data.csv'
df = pd.read_csv(file_to_import)
df.columns = ['country', 'year', 'life_expectancy', 'gdp']

#Select data for each countries 
def data_country(country):
    df_country = df[df['country']==country]
    return df_country

#Life expectancy per year and for each country // gdp per year and for each country 
x_values = data_country('China')['year']
plt.figure(figsize = (12,8))

ax1 = plt.subplot(1,2,1)
plt.xticks(x_values)
plt.plot(x_values, data_country('Chile')['life_expectancy'])
plt.plot(x_values, data_country('China')['life_expectancy'])
plt.plot(x_values, data_country('Germany')['life_expectancy'])
plt.plot(x_values, data_country('Mexico')['life_expectancy'])
plt.plot(x_values, data_country('United States of America')['life_expectancy'])
plt.plot(x_values, data_country('Zimbabwe')['life_expectancy'])
plt.ylabel('Life expectancy')
plt.title('Life expectancy per year')
plt.legend(['Chile', 'China', 'Germany', 'Mexico', 'USA', 'Zimbabwe'])

ax1 = plt.subplot(1,2,2)
plt.xticks(x_values)
plt.plot(x_values, data_country('Chile')['gdp'])
plt.plot(x_values, data_country('China')['gdp'])
plt.plot(x_values, data_country('Germany')['gdp'])
plt.plot(x_values, data_country('Mexico')['gdp'])
plt.plot(x_values, data_country('United States of America')['gdp'])
plt.plot(x_values, data_country('Zimbabwe')['gdp'])
plt.ylabel('GDP')
plt.title('GDP per year')
plt.legend(['Chile', 'China', 'Germany', 'Mexico', 'USA', 'Zimbabwe'])

plt.show()

#Average Life expectancy per average gdp from 2000 to 2015 for each country 
synthetic = df.groupby('country').mean().reset_index()
sns.set_palette('deep')
sns.scatterplot(data = synthetic, x = 'life_expectancy', y='gdp', hue = 'country')
plt.xticks(synthetic['life_expectancy'])
plt.yticks(synthetic['gdp'])
plt.title('GDP and life expectancy per country - average from 2000 to 2015')
plt.show()


#Life expectancy per gdp from 2000 to 2015 for each country (detail)
plt.figure(figsize = (10,8))
sns.set_palette('deep')
sns.scatterplot(data = df, x = 'life_expectancy', y='gdp', hue = 'country')
plt.xticks(synthetic['life_expectancy'])
plt.yticks(synthetic['gdp'])
plt.title('GDP and life expectancy per country - from 2000 to 2015')
plt.show()
