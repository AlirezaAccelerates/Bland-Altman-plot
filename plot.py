import numpy as np
import matplotlib.pyplot as plt

def bland_altman_plot(data1, data2):
    """
    Create a Bland-Altman plot to assess the agreement between two datasets.
    
    Parameters:
    data1 : array-like
        First dataset to compare.
    data2 : array-like
        Second dataset to compare.
        
    Returns:
    md : float
        Mean difference (bias).
    sd : float
        Standard deviation of the differences.
    rmse : float
        Root mean square error of the differences.
    upper_limit : float
        Upper limit of agreement (mean + 1.96 * standard deviation).
    lower_limit : float
        Lower limit of agreement (mean - 1.96 * standard deviation).
    max_abs_bland_altman_limit : float
        Maximum absolute Bland-Altman limit (max of |upper limit| or |lower limit|).
    """
    
    # Convert inputs to NumPy arrays and handle missing values
    data1 = np.asarray(data1)
    data2 = np.asarray(data2)
    
    # Calculate mean of the two datasets and the difference
    mean_values = np.nanmean([data1, data2], axis=0)
    differences = data1 - data2
    rmse = np.sqrt(np.nanmean((differences) ** 2))
    
    # Compute the mean and standard deviation of the differences
    mean_diff = np.nanmean(differences)
    std_diff = np.nanstd(differences, axis=0)
    
    # Create Bland-Altman plot
    plt.scatter(mean_values, differences)
    plt.axhline(mean_diff, color='gray', linestyle='--', label='Mean Difference')
    plt.axhline(mean_diff + 1.96 * std_diff, color='red', linestyle='--', label='Mean + 1.96 SD')
    plt.axhline(mean_diff - 1.96 * std_diff, color='red', linestyle='--', label='Mean - 1.96 SD')
    
    # Set labels
    plt.xlabel('Mean of Data1 and Data2')
    plt.ylabel('Difference between Data1 and Data2')
    
    # Dynamically set x-position for annotations based on the max value of the mean
    x_position = np.max(mean_values) * 1.02  # Slightly offset from the highest value - adjust accordingly
    
    # Add annotations for the mean and Bland-Altman limits
    plt.text(x_position, float(mean_diff), f'{float(mean_diff):.2f}', color='gray', va='center')
    plt.text(x_position, float(mean_diff + 1.96 * std_diff) + 1, f'{float(mean_diff + 1.96 * std_diff):.2f}', color='red', va='center')
    plt.text(x_position, float(mean_diff - 1.96 * std_diff) - 1, f'{float(mean_diff - 1.96 * std_diff):.2f}', color='red', va='center')
    
    # Show legend and plot
    plt.legend()
    plt.show()

    # Calculate upper and lower limits of agreement
    upper_limit = mean_diff + 1.96 * std_diff
    lower_limit = mean_diff - 1.96 * std_diff
    
    # Calculate the Max Absolute Bland-Altman Limits (MABL)
    max_abs_bland_altman_limit = max(abs(upper_limit), abs(lower_limit))
    
    return mean_diff, std_diff, rmse, upper_limit, lower_limit, max_abs_bland_altman_limit
