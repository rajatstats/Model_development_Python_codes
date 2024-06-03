
# Scatter plot between two continuous variable
# Mean value of variable on y axis and on x axis the different bins of a variable
# histogram of variable
# Subplots of multiple features with the target variable 

# Set the axis label, title of plot, gridline, legend, line style, set plot size 

def scatter_plot(x= , y= , data = , label=, marker=, c=, alpha=, xlabel=, ylabel=,title= figure_size = ,
                 loc=,fontsize= ):
    '''
    ------
    Function will create the scatter plot between two variable along with the customization of different 
    parameter for figure
    ------
    Arguments of the function are as below
    ------
    x = String with the column name of the dataframe or pandas Series which will be in the x-axis of plot 
    y = String with the column name of the dataframe or pandas Series which will be in the y-axis of plot
    data = Dataframe with the available column name x,y or it can be blank there are series passed in x,y
    label = 
    marker = 
    c = 
    alpha = 
    xlabel = 
    ylabel = 
    title = 
    loc = 
    fontsize = 
    -------
    Examples of the functions are: -
    >>>
    >>>
    >>>
    '''
    try:
        import matplotlib.pyplot as plt

        plt.plot()
        plt.scatter(x='no_atms_on_site', y='no_debit_cards',data= df,alpha=0.8,
                    label='Count_of_debit_card',marker='*',c='r')
        # plt.plot('no_debit_cards', data=df)
        plt.xlabel('no_atms_on_site')
        plt.ylabel('no_debit_cards')
        plt.title('Comparison of Total ATM Vs Total debit card')
        plt.legend(loc="lower right",fontsize='xx-small')
        plt.show()
    
    except Exception as e:
        return print(e)



 
 
