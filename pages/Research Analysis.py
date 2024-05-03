
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# Assuming the data has already been loaded somewhere in the script
# For example:
def load_csv_file(file_path, encoding='utf-8'):
    try:
        return pd.read_csv(file_path, encoding=encoding)
    except UnicodeDecodeError as e:
        st.error(f"Failed to load file {file_path} with encoding {encoding}: {e}")
        return None

# Example usage in your app
salary_df = load_csv_file(r'nba_2022-23_all_stats_with_salary.csv', 'ISO-8859-1')
final_df = load_csv_file(r'final_merged_data.csv', 'ISO-8859-1')
new_df = load_csv_file(r"new_merged_data.csv",'ISO-8859-1')
# Split the first row to create column names
original_column = final_df.columns
column_names = original_column[0].split(',')
# Now split all remaining rows into separate columns
new_df = final_df[final_df.columns[0]].str.split(',', expand=True)

# Assign the new column names to the DataFrame
new_df.columns = column_names
for column in new_df.columns:
    new_df[column] = pd.to_numeric(new_df[column], errors='ignore')


    
def load_csv_file(file_path):
    encodings = ['utf-8', 'ISO-8859-1', 'cp1252']
    for encoding in encodings:
        try:
            return pd.read_csv(file_path, encoding=encoding)
        except UnicodeDecodeError:
            continue
    st.error(f"All encodings failed for file {file_path}. Check the file encoding.")
    return None



def display_correlation():
    # Ensure 'final_df' is the DataFrame you are referring to
    if 'PTS_x' in new_df.columns:
        corr = new_df[['PTS_x', 'TRB_x', 'AST_x', 'FG%_x', 'WS_x', 'WS/48_x', 'Salary']].corr()
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
        plt.title('Correlation between Performance Metrics and Salary')
        st.pyplot(plt)
    else:
        st.error('Required columns are not present in the DataFrame.')


def display_violin_plot():
        #print(new_df.columns)
    # Define bins and labels for the points per game categories
        bins = [0, 10, 20, 30, 40]
        labels = ['0-10', '11-20', '21-30', '31-40']
        #new_df.iloc[:, 0] #yes
        print(type(new_df))

        new_df['PTS_x_category'] = pd.cut(new_df['PTS_x'], bins=bins, labels=labels, include_lowest=True)
        plt.figure(figsize=(12, 8))
        sns.violinplot(x='PTS_x_category', y='Salary', data=new_df)
        plt.title('Violin Plot of Salary Distribution Across Points Per Game Categories')
        plt.xlabel('Points Per Game')
        plt.ylabel('Salary')

        st.pyplot(plt)

new_df['Total_Games'] = new_df['W'] + new_df['L']
new_df['Win_Rate'] = new_df['W'] / new_df['Total_Games']
def plot_win_shares_vs_win_rate(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='WS_x', y='Win_Rate', data=new_df)
    plt.title('Impact of Win Shares on Team Win Rate')
    plt.xlabel('Win Shares')
    plt.ylabel('Win Rate')
    st.pyplot(plt)  # Use Streamlit's pyplot to show the plot

def plot_per_vs_win_rate(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='PER', y='Win_Rate', data=new_df)
    plt.title('Impact of Player Efficiency Rating on Team Win Rate')
    plt.xlabel('Player Efficiency Rating')
    plt.ylabel('Win Rate')
    st.pyplot(plt)  # Use Streamlit's pyplot to show the plot


def plot_salary_vs_points(data):
    # Define the color palette for the plot
    palette = ['blue', 'green', 'red', 'purple', 'orange', 'yellow', 'brown', 'pink', 'gray', 'cyan']

    # Create a linear model plot
    sns.lmplot(x='PTS', y='Salary', data=salary_df, hue='Position', palette=palette, aspect=1.5)
    plt.title('Salary vs. Points Scored by Position')
    plt.xlabel('Points Per Game')
    plt.ylabel('Salary')

    # Streamlit uses st.pyplot() to display matplotlib figures
    st.pyplot(plt)


def plot_salary_vs_minutes(data):
    # Define the color palette for the plot
    palette = ['blue', 'green', 'red', 'purple', 'orange', 'yellow', 'brown', 'pink', 'gray', 'cyan']

    # Create a linear model plot
    g = sns.lmplot(x='Total Minutes', y='Salary', data=salary_df, hue='Position', palette=palette, aspect=1.5)
    plt.xlabel('Total minutes per season')
    plt.ylabel('Salary')
    plt.title('NBA Salaries in Relation to Playing Time by Position for the 2022-2023 Season')

    # Display the plot in Streamlit
    st.pyplot(plt)


def plot_vorp_vs_salary(data):
    plt.figure(figsize=(10, 6))  # Optional: Adjust the figure size as needed
    plt.scatter(x=salary_df["Salary"], y=salary_df["VORP"], marker='o', s=3)
    plt.xlabel('Salary (Millions USD)')
    plt.ylabel('Value Over Replacement Player (VORP)')
    plt.title('Salary Correlation with VORP for the 2022-23 Season')

    # Annotate specific players based on conditions
    for i, row in salary_df.iterrows():
        if row["VORP"] > 3.6 or row["Salary"] > 40000000:
            plt.annotate(row['Player Name'], (row['Salary'], row['VORP']), textcoords='offset points', xytext=(0, 3),
                         ha='center', fontsize=6)

    st.pyplot(plt)  # Show plot in Streamlit
    plt.clf()  # Clear the figure to avoid overlap in future calls



def main():
    st.sidebar.title("Analysis")
    selected_page = st.sidebar.radio("Go to", ["NBA Player salary VS NBA player performance(Points per game)", "Does a player's playing time have any related with their salary?",
                                               "Team Win Rate VS Player Efficiency Rating"])

    if selected_page == "Home":
        home_page()
    elif selected_page == "NBA Player salary VS NBA player performance(Points per game)":
        display_violin_plot()
        st.markdown("""
                **Insights from the Violin Plot of Salary Distribution:**

                - **Points 0-10 and 11-20 (points per game):** 
                    The salary distributions for these two groups are similar, with a wide range indicating differences in the salaries of players in these scoring bands. There appears to be little difference in median salaries between these two groups.

                - **Points 21-30:**
                    The median salary is significantly higher, and the top of the salary distribution is slightly narrower compared to the previous groups. This suggests that players with scoring averages between 21-30 points per game tend to have higher salaries. However, the distribution is still quite broad, suggesting that there is a great deal of variation within the group.

                - **Points 31-40 Points:**
                    The distribution is significantly different from the other groups, with a narrower shape, suggesting less variation in salaries. This group has the highest median salary, reflecting the fact that the top scorers in this group are among the highest paid players.
                """, unsafe_allow_html=True)
        plot_salary_vs_points(salary_df)
        st.markdown("""
                **Insights from the Points vs. Salary Analysis:**

                - As we can see, there's a **positive correlation between 'Points Per Game' and 'Salary'** across different positions, as evidenced by the upward trajectory of the regression lines. This indicates that players who score more generally earn higher salaries.

                - **Salary Cap and Maximum Contracts:** The ceiling on the higher salaries could be due to salary cap restrictions or max contract amounts, which prevent salaries from rising indefinitely with points scored.
                """, unsafe_allow_html=True)
    elif selected_page == "Does a player's playing time have any related with their salary?":
        display_correlation()
        plot_salary_vs_minutes(salary_df)
        st.markdown("""
                **Insights from the Total Minutes vs. Salary Analysis:**

                - There appears to be a **positive trend** between the total minutes played and the player's salary. Players who log more minutes on the court generally earn higher salaries.

                - This suggests that players who are central to gameplay and are frequently utilized are valued higher. It reinforces the idea that on-court time is an important factor in player compensation.

                - However, it is important to note that while on-court time correlates with higher pay, it is not the sole factor determining salaries. Other elements such as player efficiency, market dynamics, team salary cap, and contractual negotiations also play significant roles.
                """, unsafe_allow_html=True)

    elif selected_page == "Team Win Rate VS Player Efficiency Rating":
        plot_win_shares_vs_win_rate(new_df)
        plot_per_vs_win_rate(new_df)
        st.dataframe(salary_df)
        plot_vorp_vs_salary(salary_df)


if __name__ == "__main__":
    main()

