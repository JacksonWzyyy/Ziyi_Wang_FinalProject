


import streamlit as st

tab1, tab2 = st.tabs(["Main Page", "Dataset Description"])

with tab1:
    st.markdown("""
                    ## Welcome to the My Final Project: The Value of Victory: Examining the Relationship Between NBA Players' Salaries, Performance, and Team Success


                    ### About
                    Welcome to my analytical exploration into the complex dynamics of the NBA, where player performance, salary structures, and team success intersect. This project seeks to uncover the nuanced relationships between how well players perform on the court, the salaries they earn, and the overall success of their teams during the 2022-23 NBA season.
                    
                    ### Developer Information
                    - **Name**: Ziyi Wang
                    - **Contact Email**: [zwang706@usc.edu](mailto:zwang706@usc.edu)

                    ### How to Use This Webapp
                    Explore various features of the app designed to facilitate interactive data analysis:

                    - **Main Page**:
                        This page contains essential information including project overview, key findings, conclusions, and developer contact information.
        
                    - **Additonal Questions Page**:
                         An additional page to answer some problems about the final project.

                    - **Data Exploration Page**:
                        Users can interact with the sidebar to select parameters from datasets. The app dynamically generates visualizations based on these selections, highlighting potential correlations between the chosen data points.

                        On a secondary tab within this page, separate plots visualize each dataset independently. This arrangement aids in understanding the complexities and unique characteristics of each dataset, enhancing the analytical experience.

                    ### Conclusion
                    In investigating the relationship between NBA players' salaries and their on-the-field performance, we observed a consistent positive correlation across various metrics. Players with more playing time, higher point totals per game, and a greater Value Over Replacement Player (VORP) generally command higher salaries, underscoring the principle that in-league compensation aligns with key performance indicators.
                    Despite the clear trends, our analyses also reveal considerable variability and several outliers, indicating that salaries are not solely a function of these performance variables. Factors such as contractual negotiations, marketability, team financial strategies, and perhaps even a player's off-the-court influence, all contribute to the multifaceted nature of salary determination in professional basketball.
                    Furthermore, regarding Does individual player performance impact a team’s wins? Yes, there is a clearer positive correlation between Win Shares and team win rate, indicating that players who contribute more directly to their team's success (as quantified by Win Shares) tend to be on teams with higher win rates. Also, there is a positive relationship between PER and team win rate, suggesting that more efficient players tend to contribute to better team performance, though the correlation is not as pronounced as with Win Shares.
                    However, while the trends are generally positive, there are variations and outliers in the data that suggest other factors also significantly influence team success. Team strategy, the overall team composition, injuries, and the strength of the competition are likely also important.
                    
                     ### Major Gotchas
                    - **Visualization Load Time**: Some visualizations may take a few moments to load, especially for larger datasets.
                    - **Data Scope Limitation**: One of my issues is that my intention was towards comparing the values of all the datasets, not just the top 10 level MVP players, but after doing the combined dataset, I only got data for 10 players, and while this doesn't affect the exploration, it's a major consideration to be aware of.

                    
                    ### Navigation Tips
                    - Utilize the sidebar to switch between different analysis sections.
                    - Access specific dataset visualizations by navigating to the respective tabs.
                    - For any queries or detailed insights, refer to the contact email provided above. If you need further assistance with navigating or using the app, don't hesitate to reach out via the email.
                    """, unsafe_allow_html=True)

with tab2:
    st.header("Data Sources Description")
    st.markdown("""
    ## Data Source 1: Basketball Reference (Player Data)
    **URL for website**: [Basketball Reference](https://www.basketball-reference.com/awards/)

    **Description**:
    'Basketball Reference' serves as an extensive online repository for basketball data, analysis, and historical insights. It offers detailed information on basketball leagues, players, teams, and accolades across NBA, NCAA, and international tournaments.
    The platform is esteemed for its comprehensive scope and reliability, providing in-depth statistical metrics, player biographies, game logs, and historical archives. It caters to enthusiasts, analysts, journalists, and scholars, making it a valuable resource within the basketball community.

    ## Data Source 2: BALLDONTLIE API (Team Data)
    **URL for API**: [BALLDONTLIE API](https://www.balldontlie.io/)
    **API Documentation**: [View Documentation](https://docs.balldontlie.io/#introduction)

    **Description**:
    The BALLDONTLIE API is an extensive source for NBA statistics and live betting odds, covering data from 1946 to the current season. It is renowned for providing comprehensive NBA data that supports a wide range of applications, from fan engagement to professional analytics.

    ## Data Source 3: NBA Player Salaries (2022-23 Season)
    **URL for CSV Download**: [Kaggle Dataset](https://www.kaggle.com/datasets/jamiewelsh2/nba-player-salaries-2022-23-season)

    **Description**:
    This dataset combines player per-game data and advanced statistics with salary information for the NBA's 2022-23 season. Key attributes include player identifiers, team affiliation, statistical performance metrics, and salary figures. It supports in-depth analyses, predictive modeling, and insights into the economic aspects of professional basketball performance.
    """, unsafe_allow_html=True)