import matplotlib
matplotlib.use('Agg')  # Use 'Agg' backend for rendering to files
import matplotlib.pyplot as plt
import seaborn as sns

def generate_heatmap(pivot_table, output_file):
    plt.figure(figsize=(12, 8))
    
    # Create the heatmap with annotations, the Blues color map, and a fixed range of 0 to 100
    ax = sns.heatmap(
        pivot_table, 
        annot=True, 
        cmap="YlGnBu", 
        linewidths=.5, 
        cbar_kws={'label': 'QA Score'}, 
        vmin=50, 
        vmax=100,
        annot_kws={"size": 14}
    )
    
    # Set the title of the heatmap
    plt.title('Agent Behavior Heatmap by Interaction Type', fontsize=18, fontweight='bold')
    
    # Add labels to the axes and increase their font size and weight
    ax.set_xlabel('Interaction Type', fontsize=16, fontweight='bold')
    ax.set_ylabel('Agent Name', fontsize=16, fontweight='bold')
    
    # Increase the font size of the tick labels on both axes
    ax.tick_params(axis='both', which='major', labelsize=14)
    
    # Save the heatmap to the specified file
    plt.savefig(output_file)
    plt.close()