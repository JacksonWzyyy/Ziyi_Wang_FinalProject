import streamlit as st
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tab1, tab2 = st.tabs(["Additonal Questions ", 'Interactive tab'])

with tab1:
    # Page Title
    st.title('Additonal question answers and Reflection')

    st.markdown("""
    ### What did you set out to study?
    The primary goal of my final project was to explore and quantify the relationships between NBA players' salaries, their individual performance metrics, and their teams' success in the league. Specifically, the project aimed to address two main research questions:
    
    1. Does salary correlate with on-the-field performance? This part of the study focused on understanding whether higher salaries are indicative of better individual performance in terms of scoring, assists, rebounds, and other statistical measures that contribute to a player's overall effectiveness on the court.
    
    2. Does individual player performance impact a team’s wins? The second focus was to analyze how much individual player's performance metrics contribute to their team's overall success, measured in wins and losses during the season. This involved examining whether teams with higher-performing players (according to various metrics) tend to win more games, thereby assessing the value of individual contributions to team success.
    """, unsafe_allow_html=True)

    st.markdown("""
    ### What did you discover and conclude?
    
    My analysis revealed several key findings regarding the relationship between NBA player salaries, performance metrics, and team success:
    
    - There exists a consistent positive correlation between player salaries and on-the-field performance metrics such as points per game, rebounds, assists, and Win Shares. Players who contribute more to their team's success tend to command higher salaries.
    - Individual player performance, as quantified by metrics like Win Shares and Player Efficiency Rating (PER), has a notable impact on their team's win rate. Teams with higher-performing players tend to win more games, suggesting the importance of individual contributions to overall team success.
    - However, I also observed variability and outliers in the data, indicating that salary determination and team success are influenced by factors beyond individual performance. These may include contractual negotiations, marketability, team financial strategies, and the overall composition of the team.
    - Despite these complexities, my analysis confirms the significance of on-the-field performance in shaping player salaries and team success in the NBA.
    """, unsafe_allow_html=True)

    st.markdown("""
    ### What difficulties did you encounter in completing the project?
    
    While conducting this project, I encountered several challenges that impacted our progress:
    
    - **Data Acquisition:** Obtaining comprehensive and clean datasets was a significant challenge. I had to merge data from multiple sources and ensure consistency and accuracy in our analysis.
    - **Data Preprocessing:** Cleaning and preprocessing the data required substantial time and effort. I encountered difficulties, particularly when loading the merged final_df DataFrame. Despite successful preprocessing in JupyterLab, Streamlit struggled to read column values. To address this, I split the first row to create column names and split all remaining rows into separate columns. Then assigned the new column names to the DataFrame, enabling Streamlit to interpret the data correctly.
    - **Statistical Analysis:** Conducting robust statistical analysis required a deep understanding of both basketball analytics and statistical methodologies. Ensuring the validity and reliability of my results demanded careful consideration of various statistical techniques.
    - **Interpretation:** Interpreting the results and drawing meaningful conclusions from the data required critical thinking and domain expertise. I had to contextualize our findings within the broader landscape of NBA analytics and player evaluation.
    """, unsafe_allow_html=True)

    st.markdown("""
    ### What skills did you wish you had while you were doing the project?
    
    While working on this project, I identified several skills that would have enhanced my ability to tackle challenges and analyze the data more effectively:
    
    - **Machine Learning:** Stronger machine learning skills, including familiarity with advanced algorithms, model evaluation techniques, and hyperparameter tuning, would have enabled me to develop more sophisticated predictive models and extract deeper insights from the data.
    - **Advanced Visualization:** Enhanced proficiency in advanced data visualization libraries such as Plotly, Bokeh, or D3.js would have allowed me to create more interactive and visually compelling visualizations, enabling clearer communication of insights to stakeholders.
    - **Statistical Analysis:** Further expertise in statistical analysis methods, including hypothesis testing, regression analysis, and Bayesian inference, would have provided a more robust foundation for exploring relationships within the data and deriving meaningful conclusions.
    """, unsafe_allow_html=True)

    st.markdown("""
    ### What would you do next to expand or augment the project?
    
    To expand and augment the project further, I would consider the following steps:
    
    - **Incorporate Additional Data Sources:** Integrate additional datasets such as player injury records, team performance metrics over multiple seasons, or demographic data to provide a more comprehensive analysis of the factors influencing player salaries and team success.
    
    - **Advanced Modeling Techniques:** Explore advanced machine learning models such as ensemble methods, deep learning architectures, or reinforcement learning algorithms to improve prediction accuracy and uncover more intricate patterns in the data.
    
    - **Real-time Data Integration:** Implement real-time data integration pipelines to continuously update the analysis with the latest NBA player statistics and team performance metrics, enabling timely insights and trend monitoring throughout the NBA season.
    """, unsafe_allow_html=True)

with tab2:
    def load_csv_file(file_path):
        encodings = ['utf-8', 'ISO-8859-1', 'cp1252']
        for encoding in encodings:
            try:
                return pd.read_csv(file_path, encoding=encoding)
            except UnicodeDecodeError:
                continue
        st.error(f"All encodings failed for file {file_path}. Check the file encoding.")
        return None

    salary_df = load_csv_file(r'./nba_2022-23_all_stats_with_salary.csv')
    final_df = load_csv_file(r'./final_merged_data.csv')
    new_df = load_csv_file(r"./new_merged_data.csv")
    # Split the first row to create column names
    original_column = final_df.columns
    column_names = original_column[0].split(',')
    # Now split all remaining rows into separate columns
    new_df = final_df[final_df.columns[0]].str.split(',', expand=True)

    # Assign the new column names to the DataFrame
    new_df.columns = column_names
    for column in new_df.columns:
        new_df[column] = pd.to_numeric(new_df[column], errors='ignore')

    choice = ['PTS_x', 'TRB_x', 'AST_x', 'PER','STL_x','BLK_x','FG%_x','3P%_x']
    feature_fromuser = st.sidebar.multiselect('Select feature', choice, default = ['PTS_x', 'PER'])
    points_fromuser = st.sidebar.slider('Select Points Per Game', 0, 40, (10,22))

    visual_df_mask = (new_df['PER'] > points_fromuser[0]) & (new_df['PER'] < points_fromuser[1]) #and new_df['PER'] >points_fromuser[1]
    visual_df = new_df[visual_df_mask]

    choice_corr = ['PTS_x', 'TRB_x', 'AST_x', 'FG%_x', 'WS_x', 'WS/48_x', 'Salary']
    corr_fromuser = st.sidebar.multiselect('Select correlation feature', choice_corr, default = ['PTS_x', 'TRB_x', 'AST_x'])
    st.sidebar.markdown("Please make your selections above and press 'Submit' below to display the results, will show in Interactive tab.")

    if st.sidebar.button("submit"):
        # st.write("")
        st.dataframe(visual_df[feature_fromuser])
        corr = new_df[corr_fromuser].corr()
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
        plt.title('Correlation between Performance Metrics and Salary')
        st.pyplot(plt)







