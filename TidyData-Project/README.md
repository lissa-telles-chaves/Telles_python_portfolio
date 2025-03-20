# Tidy Data:
Here we reorganized data regarding who are the medalists of the 2008 Olympics into a more digestible dataframe and then proceeded to make an EDA to further help us understand the data.
## 📖 Tidy Data Principles Sparknotes:
In portuguese there is a famous song from the 2000's which says that everything must be in their respectives space(link: https://open.spotify.com/track/15llrnGADRZYnA39AYQHIL?si=ca26f20223094db8 ), in many ways, the principles lead us to a similar conclusion as it states that:
- Each variable forms a column
- Each observation forms a row
- Each type of observational unit forms a table
## 👩🏻‍🏫 Instructions:
To run the notebook, I recommend following the order it is presented in, running all the previous code before the markdown cell with the message "begin EDA". If you desire to look only at one of the plots, there are no dependencies issues there, thus, if you wish to run only Plot 1 or only Plot 2 you will face no issues whatsover.
However, one dependency in this notebook is the need of having all the following libraries to guarantee the functionality of the code. 

### 📚 libraries utilized
- seaborn
- matplot (make sure to also import rc from matplotlib just to be safe
- pandas
- numpy

## 📊 EDA plots:

plot 1 - heatmap: Representation of male and female athletes across 10 sports
![Alt text](https://github.com/lissa-telles-chaves/Telles_python_portfolio/blob/63742ec03972da48551988d79950eb8b7c3ab15f/TidyData-Project/malefemalerepsports.png)

plot 2 - stacked bar plot: Number of Medals by Sport

![Alt text](https://github.com/lissa-telles-chaves/Telles_python_portfolio/blob/63742ec03972da48551988d79950eb8b7c3ab15f/TidyData-Project/stackedbarplot_medalxsport.png)

### references:
Tidy Data by Hadley Wickham: https://vita.had.co.nz/papers/tidy-data.pdf
Pandas_Cheat_Sheet: https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

