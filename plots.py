
# Scatter plot between two continuous variable
# Mean value of variable on y axis and on x axis the different bins of a variable
# histogram of variable
# Subplots of multiple features with the target variable 
# Set the axis label, title of plot, gridline, legend, line style, set plot size 



##------------------------------------Code for scatter plot begin -----------------------------------------
import matplotlib.pyplot as plt

def scatter_plot(x , y, data, label, marker, c, alpha, xlabel, ylabel,title,figure_size,
                 loc,fontsize ):
    """
    ----------------------------------------------------------------------------------------------
    Function will create the scatter plot between two variable along with the customization of different 
    parameter for figure
    ----------------------------------------------------------------------------------------------
    Arguments of the function are as below
    ----------------------------------------------------------------------------------------------
    x : String with the column name of the dataframe or pandas Series which will be in the x-axis of plot 
    y : String with the column name of the dataframe or pandas Series which will be in the y-axis of plot
    data : Dataframe with the available column name x,y or it can be blank there are series passed in x,y
    label : String with details of y value pointers
    marker : https://matplotlib.org/stable/api/markers_api.html refer this for different marker
    c : https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def refer for different color option
    alpha : The alpha blending value, between 0 (transparent) and 1 (opaque).
    xlabel : x-axis name
    ylabel : y-axis name
    title : title of the plot 
    figure_size  : tuple input eg. (4,4)
    loc :location of the legend The strings 'upper left', 'upper right', 'lower left', 'lower right' place the 
        legend at the corresponding corner of the axes.The strings 'upper center', 'lower center','center left', 'center right' place the legend at the center of the corresponding edge of the axes.
    fontsize : String with any of the value based on preference {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'} 
    -----------------------------------------------------------------------------------------------
    Examples of the functions are: -

    >>> scatter_plot(x='grade' , y='member_id', data=data, label='member_id', marker='*', c='r', alpha=0.5, 
             xlabel='grade', ylabel='member_id',title='Count of distinct member_id per grade',figure_size=(6,6),
                 loc='upper right',fontsize='xx-small')
    >>> Ouput a scatter plot in the notebook
    
    """
    try:
        plt.figure(figsize=figure_size)
        plt.plot()
        plt.scatter(x=x, y=y,data=data,label=label,marker=marker,c=c)
        # plt.plot('no_debit_cards', data=df)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.legend(loc=loc,fontsize=fontsize)
        plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)#axis='x' or 'y' will create corresponding grid
        plt.show()
    
    except Exception as e:
        print(e)

##------------------------------------Code for scatter plot end -----------------------------------------
#########################################################################################################
##------------------------------------Code for line plot begin ------------------------------------------
def line_plot(x , y, data, label, marker, c, alpha, xlabel, ylabel,title,figure_size,
                 loc,fontsize ):
    """
    ----------------------------------------------------------------------------------------------
    Function will create the scatter plot between two variable along with the customization of different 
    parameter for figure
    ----------------------------------------------------------------------------------------------
    Arguments of the function are as below
    ----------------------------------------------------------------------------------------------
    x : String with the column name of the dataframe or pandas Series which will be in the x-axis of plot 
    y : String with the column name of the dataframe or pandas Series which will be in the y-axis of plot
    data : Dataframe with the available column name x,y or it can be blank there are series passed in x,y
    label : String with details of y value pointers
    marker : https://matplotlib.org/stable/api/markers_api.html refer this for different marker
    c : https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def refer for different color option
    alpha : The alpha blending value, between 0 (transparent) and 1 (opaque).
    xlabel : x-axis name
    ylabel : y-axis name
    title : title of the plot 
    figure_size  : tuple input eg. (4,4)
    loc :location of the legend The strings 'upper left', 'upper right', 'lower left', 'lower right' place the 
        legend at the corresponding corner of the axes.The strings 'upper center', 'lower center','center left', 'center right' place the legend at the center of the corresponding edge of the axes.
    fontsize : String with any of the value based on preference {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'} 
    -----------------------------------------------------------------------------------------------
    Examples of the functions are: -

    >>> line_plot(x='grade' , y='member_id', data=data, label='member_id', marker='*', c='r', alpha=0.5, 
             xlabel='grade', ylabel='member_id',title='Count of distinct member_id per grade',figure_size=(6,6),
                 loc='upper right',fontsize='xx-small')
    >>> Ouput a scatter plot in the notebook
    
    """
    try:
        plt.figure(figsize=figure_size)
        plt.plot(x, y,data=data,label=label,marker=marker,c=c,linestyle=':')
        # plt.plot('no_debit_cards', data=df)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.legend(loc=loc,fontsize=fontsize)
        plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)#axis='x' or 'y' will create corresponding grid
        plt.show()
    
    except Exception as e:
        print(e)
##------------------------------------Code for line plot end --------------------------------------------
#########################################################################################################
##------------------------------------Code for bar plot begin --------------------------------------------
def bar_plot(x , y, data, width,c,edgecolor,linewidth,alpha, xlabel, ylabel,title,figure_size,
             labels,loc,fontsize, leg_title):
    """
    ----------------------------------------------------------------------------------------------
    Function will create the scatter plot between two variable along with the customization of different 
    parameter for figure
    ----------------------------------------------------------------------------------------------
    Arguments of the function are as below
    ----------------------------------------------------------------------------------------------
    x : String with the column name of the dataframe or pandas Series which will be in the x-axis of plot 
    y : String with the column name of the dataframe or pandas Series which will be in the y-axis of plot
    data : Dataframe with the available column name x,y or it can be blank there are series passed in x,y
    label : String with details of y value pointers
    marker : https://matplotlib.org/stable/api/markers_api.html refer this for different marker
    c : https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def refer for different color option
    alpha : The alpha blending value, between 0 (transparent) and 1 (opaque).
    xlabel : x-axis name
    ylabel : y-axis name
    title : title of the plot 
    figure_size  : tuple input eg. (4,4)
    loc :location of the legend The strings 'upper left', 'upper right', 'lower left', 'lower right' place the 
        legend at the corresponding corner of the axes.The strings 'upper center', 'lower center','center left', 'center right' place the legend at the center of the corresponding edge of the axes.
    fontsize : String with any of the value based on preference {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'} 
    -----------------------------------------------------------------------------------------------
    Examples of the functions are: -

    >>> bar_plot(x='grade' , y='member_id', data=data, label='member_id', marker='*', c='r', alpha=0.5, 
             xlabel='grade', ylabel='member_id',title='Count of distinct member_id per grade',figure_size=(6,6),
                 loc='upper right',fontsize='xx-small')
    >>> Ouput a scatter plot in the notebook
    
    """
    try:
        plt.figure(figsize=figure_size)
        p =plt.bar(x, y,data=data,width=width,color=c,edgecolor=edgecolor, linewidth=linewidth,alpha=alpha)
        plt.ylim((0,1.5*data.member_id.max()))
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)#axis='x' or 'y' will create corresponding grid
        plt.bar_label(p, fmt='{:,.0f}',label_type='center')
        plt.legend(labels=labels,loc=loc,fontsize=fontsize,title=leg_title)
        plt.show()
    
    except Exception as e:
        print(e)
##------------------------------------Code for bar plot end --------------------------------------------

