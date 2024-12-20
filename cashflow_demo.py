# -*- coding: utf-8 -*-
"""cashflow_demo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rMv-axvoSNDT3r17Zy-7_ugIwK8onmzV
"""

pip install --upgrade pip

!pip install streamlit pyngrok streamlit-option-menu

from pyngrok import ngrok

# Kill any existing ngrok processes
ngrok.kill()

# Set your ngrok authentication token
ngrok.set_auth_token('2pm0FE4FrUA9GPAx9giV2XPF6eN_5LQ9VenXcsjzcubNjnnWe')

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# 
# import streamlit as st
# from streamlit_option_menu import option_menu
# import pandas as pd
# import numpy as np
# import altair as alt
# 
# # Set page configuration
# st.set_page_config(
#     page_title="Apartment Cashflow Analysis",
#     page_icon="🏠",
#     layout="wide",
# )
# 
# # Inject custom CSS for gradient backgrounds and home page styling
# st.markdown(
#     """
#     <style>
#     /* Gradient background for the main content */
#     [data-testid="stAppViewContainer"] {
#         background: linear-gradient(to bottom right, #ffecd2, #fcb69f);
#     }
#     /* Gradient background for the sidebar */
#     [data-testid="stSidebar"] > div:first-child {
#         background: linear-gradient(to bottom, #004d40, #e3f2fd);
#     }
#     /* Adjust text color for better contrast in the sidebar */
#     [data-testid="stSidebar"] .css-1d391kg,
#     [data-testid="stSidebar"] .css-1v3fvcr,
#     [data-testid="stSidebar"] .css-16huue1,
#     [data-testid="stSidebar"] .css-hxt7ib {
#         color: white;
#     }
#     /* Custom styles for the home page title and subtitle */
#     .home-title {
#         font-family: 'Arial', sans-serif;
#         font-size: 3em;
#         color: #333333;
#         text-align: center;
#         border: 2px solid #333333;
#         padding: 20px;
#         margin-top: 50px;
#         background-color: rgba(255, 255, 255, 0.8);
#         border-radius: 10px;
#     }
#     .home-subtitle {
#         font-family: 'Arial', sans-serif;
#         font-size: 1.5em;
#         color: #555555;
#         text-align: center;
#         border: 1px solid #555555;
#         padding: 15px;
#         margin-top: 20px;
#         background-color: rgba(255, 255, 255, 0.7);
#         border-radius: 10px;
#     }
#     /* Adjust headers in the main content area */
#     h1, h2, h3, h4, h5, h6 {
#         color: #333333;
#     }
#     /* Adjust other text in the main content area */
#     .stMarkdown p, .stMarkdown div {
#         color: #333333;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
# 
# # Sample data creation with building and apartment names
# def create_sample_data():
#     building_names = [
#         'Basel Tower', 'Rheinfelder Hof', 'Spalentor Residence', 'St. Jakob Park',
#         'Marktplatz Apartments', 'Messe Basel', 'Barfüsserplatz Complex',
#         'University Center', 'Münsterplatz Domicile', 'Kunstmuseum Quarters',
#         'Tinguely House', 'Kleinbasel Heights', 'Grossbasel View', 'Middle Bridge Estate',
#         'Museum der Kulturen Lodge', 'Basel Zoo Residences', 'Papiermühle Manor',
#         'Beyeler Foundation Villas', 'Schifflände Suites', 'Dreiländereck Apartments',
#         'Novartis Campus Living', 'St. Alban-Graben Homes', 'Claraplatz Flats',
#         'Badischer Bahnhof Lofts', 'Botanical Garden Homes', 'Roche Tower Living',
#         'Fähreweg Apartments', 'Petersplatz Residences', 'Hammerstrasse Homes', 'Zoo Basel Villas'
#     ]
# 
#     apartment_names = [
#         'Rhine View Suite', 'City Lights Loft', 'Garden Terrace Flat', 'Penthouse Panorama',
#         'Courtyard Condo', 'Historic Charm Apartment', 'Modern Minimalist Space',
#         'Art Deco Dwelling', 'Cozy Nest', 'Luxury Living Quarters',
#         'Riverside Retreat', 'Urban Oasis', 'Sunlit Studio', 'Family Friendly Flat',
#         "Architect's Abode", 'Cultural Hub Condo', 'Designer Duplex', 'Vintage Villa',
#         'Skyline Serenity', 'Boutique Bungalow', 'Eco-Friendly Estate', 'Grand Central Flat',
#         'Rooftop Refuge', 'Secret Garden Apartment', 'Waterfront Wonder',
#         'Hillside Haven', 'Zen Zone', "Time Traveler's Flat", 'Modernist Masterpiece',
#         'Enchanted Estate', "Artists' Alcove", "Traveler's Rest", "Scholars' Suite",
#         "Nature's Nook", 'The Think Tank', 'Quiet Corner', 'Happy Home', 'Peaceful Place',
#         "Dreamer's Den", 'The Hideaway', 'Downtown Delight', 'Suburban Sanctuary',
#         'Basel Basecamp', "River's Edge", 'City Center Suite', 'Old Town Oasis',
#         'Market Square Apartment', 'Festival Flat', 'Historic Haven', 'Culinary Corner',
#         'Musical Muse', 'Sunrise Suite', 'Moonlight Manor', 'Harmony House', 'Serenity Space',
#         "Gourmet Gallery", "Artist's Loft", "Explorer's Den", "Scholar's Sanctuary", 'Mystic Manor'
#     ]
# 
#     data = []
#     building_apartments = {}
#     apartment_names_copy = apartment_names.copy()
#     np.random.shuffle(apartment_names_copy)
# 
#     months = list(range(1, 13))  # Months 1 to 12
# 
#     for building in building_names:
#         num_apartments = np.random.randint(1, 5)
#         if len(apartment_names_copy) < num_apartments:
#             apartment_names_copy = apartment_names.copy()
#             np.random.shuffle(apartment_names_copy)
#         apartments = apartment_names_copy[:num_apartments]
#         apartment_names_copy = apartment_names_copy[num_apartments:]
#         building_apartments[building] = apartments
# 
#         for apartment in apartments:
#             for month in months:
#                 costs = np.random.randint(1000, 5000, size=3)
#                 revenues = np.random.randint(2000, 7000, size=3)
#                 data.append({
#                     'Building': building,
#                     'Apartment': apartment,
#                     'Month': month,
#                     'Mietaufwand': costs[0],
#                     'Energieverbrauch': costs[1],
#                     'Sonstige Aufwände': costs[2],
#                     'Mietertrag': revenues[0],
#                     'Extra Ertrag': revenues[1],
#                     'Sonstige Erträge': revenues[2],
#                 })
# 
#     df = pd.DataFrame(data)
#     return df, building_apartments, building_names
# 
# df, building_apartments, building_names = create_sample_data()
# 
# def main():
#     # Create a custom hovering sidebar menu
#     with st.sidebar:
#         selected = option_menu(
#             menu_title="Navigation",
#             options=["Home", "Select Building", "Select Apartments", "Simplified", "Charts"],
#             icons=["house", "building", "door-open", "list", "bar-chart-line"],
#             menu_icon="cast",
#             default_index=0,
#             styles={
#                 "container": {"padding": "0!important", "background-color": "#abb6de"},
#                 "icon": {"color": "white", "font-size": "25px"},
#                 "nav-link": {
#                     "font-size": "20px",
#                     "text-align": "left",
#                     "margin": "0px",
#                     "color": "white",
#                     "--hover-color": "#c6c77d",
#                 },
#                 "nav-link-selected": {"background-color": "#004d40"},
#             },
#         )
# 
#     if selected == "Home":
#         # Apply custom classes to the title and subtitle
#         st.markdown('<div class="home-title">Apartment Cashflow Analysis</div>', unsafe_allow_html=True)
#         st.markdown('<div class="home-subtitle">Welcome to the Apartment Cashflow Analysis App</div>', unsafe_allow_html=True)
#         st.write("Use the menu to navigate through the app.")
# 
#     elif selected == "Select Building":
#         st.header("Select Building")
#         selected_building = st.selectbox("Building", building_names)
#         st.session_state['selected_building'] = selected_building
# 
#     elif selected == "Select Apartments":
#         if 'selected_building' in st.session_state:
#             selected_building = st.session_state['selected_building']
#             st.header(f"Select Apartments in {selected_building}")
#             apartments_in_building = building_apartments[selected_building]
#             selected_apartments = st.multiselect(
#                 "Apartments", apartments_in_building, default=apartments_in_building
#             )
# 
#             if selected_apartments:
#                 # Filter data for selected building and apartments
#                 building_data = df[(df['Building'] == selected_building) & (df['Apartment'].isin(selected_apartments))]
#                 selected_data = building_data.copy()
# 
#                 st.header(f"Cashflow for {selected_building}")
# 
#                 # Display cashflow for each apartment using expanders
#                 for apartment in selected_apartments:
#                     with st.expander(f"Apartment: {apartment}"):
#                         apt_data = selected_data[selected_data['Apartment'] == apartment]
# 
#                         # Calculate totals
#                         mietaufwand = apt_data['Mietaufwand'].sum()
#                         energieverbrauch = apt_data['Energieverbrauch'].sum()
#                         sonstige_aufwaende = apt_data['Sonstige Aufwände'].sum()
#                         mietertrag = apt_data['Mietertrag'].sum()
#                         extra_ertrag = apt_data['Extra Ertrag'].sum()
#                         sonstige_ertraege = apt_data['Sonstige Erträge'].sum()
# 
#                         total_costs = mietaufwand + energieverbrauch + sonstige_aufwaende
#                         total_revenues = mietertrag + extra_ertrag + sonstige_ertraege
#                         gewinn = total_revenues - total_costs
# 
#                         # Create tabs for Costs and Revenues Breakdown
#                         tabs = st.tabs(["Kostenübersicht", "Ertragsübersicht"])
# 
#                         with tabs[0]:
#                             st.markdown(f"- **Mietaufwand:** {mietaufwand}")
#                             st.markdown(f"- **Energieverbrauch:** {energieverbrauch}")
#                             st.markdown(f"- **Sonstige Aufwände:** {sonstige_aufwaende}")
#                             st.markdown(f"**Gesamtkosten:** {total_costs}")
# 
#                         with tabs[1]:
#                             st.markdown(f"- **Mietertrag:** {mietertrag}")
#                             st.markdown(f"- **Extra Ertrag:** {extra_ertrag}")
#                             st.markdown(f"- **Sonstige Erträge:** {sonstige_ertraege}")
#                             st.markdown(f"**Gesamterträge:** {total_revenues}")
# 
#                         # Display Gewinn
#                         st.markdown(f"**Gewinn:** {gewinn}")
# 
#                 # Display totals for the building inside an expander
#                 with st.expander(f"Total for {selected_building}"):
#                     total_costs = selected_data[['Mietaufwand', 'Energieverbrauch', 'Sonstige Aufwände']].sum().sum()
#                     total_revenues = selected_data[['Mietertrag', 'Extra Ertrag', 'Sonstige Erträge']].sum().sum()
#                     gewinn = total_revenues - total_costs
# 
#                     # Create tabs for Total Costs and Revenues Breakdown
#                     total_tabs = st.tabs(["Gesamtkostenübersicht", "Gesamtertragsübersicht"])
# 
#                     with total_tabs[0]:
#                         total_mietaufwand = selected_data['Mietaufwand'].sum()
#                         total_energieverbrauch = selected_data['Energieverbrauch'].sum()
#                         total_sonstige_aufwaende = selected_data['Sonstige Aufwände'].sum()
#                         st.markdown(f"- **Total Mietaufwand:** {total_mietaufwand}")
#                         st.markdown(f"- **Total Energieverbrauch:** {total_energieverbrauch}")
#                         st.markdown(f"- **Total Sonstige Aufwände:** {total_sonstige_aufwaende}")
#                         st.markdown(f"**Gesamtkosten:** {total_costs}")
# 
#                     with total_tabs[1]:
#                         total_mietertrag = selected_data['Mietertrag'].sum()
#                         total_extra_ertrag = selected_data['Extra Ertrag'].sum()
#                         total_sonstige_ertraege = selected_data['Sonstige Erträge'].sum()
#                         st.markdown(f"- **Total Mietertrag:** {total_mietertrag}")
#                         st.markdown(f"- **Total Extra Ertrag:** {total_extra_ertrag}")
#                         st.markdown(f"- **Total Sonstige Erträge:** {total_sonstige_ertraege}")
#                         st.markdown(f"**Gesamterträge:** {total_revenues}")
# 
#                     # Display Gewinn
#                     st.markdown(f"**Gewinn:** {gewinn}")
#             else:
#                 st.write("Please select at least one apartment to display cashflow.")
#         else:
#             st.write("Please select a building first from 'Select Building' tab.")
# 
#     elif selected == "Simplified":
#         st.header("Simplified View of All Apartments")
# 
#         for building in building_names:
#             with st.expander(f"Building: {building}"):
#                 # Get data for this building
#                 building_data = df[df['Building'] == building].copy()
# 
#                 # Calculate total costs, revenues, and Gewinn per apartment
#                 building_data['Gesamtkosten'] = building_data[['Mietaufwand', 'Energieverbrauch', 'Sonstige Aufwände']].sum(axis=1)
#                 building_data['Gesamterträge'] = building_data[['Mietertrag', 'Extra Ertrag', 'Sonstige Erträge']].sum(axis=1)
#                 building_data['Gewinn'] = building_data['Gesamterträge'] - building_data['Gesamtkosten']
# 
#                 # Aggregate data by apartment
#                 aggregated_data = building_data.groupby('Apartment').sum().reset_index()
# 
#                 # Create a DataFrame to display all costs and revenues
#                 simplified_df = aggregated_data[['Apartment',
#                                                  'Mietaufwand', 'Energieverbrauch', 'Sonstige Aufwände',
#                                                  'Mietertrag', 'Extra Ertrag', 'Sonstige Erträge',
#                                                  'Gesamtkosten', 'Gesamterträge', 'Gewinn']]
# 
#                 # Display the DataFrame
#                 st.table(simplified_df)
# 
#                 # Calculate totals for the building
#                 total_costs = aggregated_data['Gesamtkosten'].sum()
#                 total_revenues = aggregated_data['Gesamterträge'].sum()
#                 total_gewinn = aggregated_data['Gewinn'].sum()
# 
#                 st.markdown(f"**Gesamtkosten for {building}:** {total_costs}")
#                 st.markdown(f"**Gesamterträge for {building}:** {total_revenues}")
#                 st.markdown(f"**Gewinn for {building}:** {total_gewinn}")
# 
#     elif selected == "Charts":
#         st.header("Charts")
# 
#         if 'selected_building' in st.session_state:
#             selected_building = st.session_state['selected_building']
#         else:
#             st.write("Please select a building first from 'Select Building' tab.")
#             return
# 
#         st.header(f"Charts for {selected_building}")
#         building_data = df[df['Building'] == selected_building]
#         apartments_in_building = building_apartments[selected_building]
# 
#         for apartment in apartments_in_building:
#             apt_data = building_data[building_data['Apartment'] == apartment].copy()
# 
#             # Calculate total costs, revenues, and Gewinn per month
#             apt_data['Gesamtkosten'] = apt_data[['Mietaufwand', 'Energieverbrauch', 'Sonstige Aufwände']].sum(axis=1)
#             apt_data['Gesamterträge'] = apt_data[['Mietertrag', 'Extra Ertrag', 'Sonstige Erträge']].sum(axis=1)
#             apt_data['Gewinn'] = apt_data['Gesamterträge'] - apt_data['Gesamtkosten']
# 
#             # Now, plot the data
#             with st.expander(f"Apartment: {apartment}"):
#                 # Create a DataFrame for plotting
#                 plot_data = apt_data[['Month', 'Gesamtkosten', 'Gesamterträge', 'Gewinn']].sort_values('Month')
#                 plot_data = plot_data.melt('Month', var_name='Category', value_name='Amount')
# 
#                 # Create the chart using Altair
#                 chart = alt.Chart(plot_data).mark_line(point=True).encode(
#                     x=alt.X('Month:O', title='Month'),
#                     y=alt.Y('Amount', title='Amount'),
#                     color=alt.Color('Category', scale=alt.Scale(
#                         domain=['Gesamtkosten', 'Gesamterträge', 'Gewinn'],
#                         range=['red', 'blue', 'green']
#                     )),
#                     tooltip=['Month', 'Category', 'Amount']
#                 ).properties(
#                     width=600,
#                     height=400,
#                     title=f"Financial Overview for {apartment}"
#                 )
# 
#                 st.altair_chart(chart, use_container_width=True)
#     else:
#         st.write("Please select a valid option from the navigation menu.")
# 
# if __name__ == "__main__":
#     main()
#

import subprocess
import time
from pyngrok import ngrok

# Start the Streamlit app in the background
process = subprocess.Popen(
    ['streamlit', 'run', 'app.py', '--server.port', '8501', '--server.enableCORS', 'false', '--server.enableXsrfProtection', 'false'],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Wait for the Streamlit app to start
# Depending on the complexity of your app, you might need to adjust the sleep time
time.sleep(10)

# Check if the Streamlit app started successfully
stdout, stderr = process.communicate(timeout=1) if process.poll() is not None else (b'', b'')

if process.poll() is None:
    # Process is still running
    print("Streamlit app is running...")
else:
    # Process has terminated
    print("Streamlit app failed to start.")
    print(stderr.decode())
    # Terminate the ngrok process if any
    ngrok.kill()
    # Exit the notebook cell
    raise SystemExit("Streamlit app failed to start.")

# Start ngrok tunnel
public_url = ngrok.connect(8501)
print(f"Public URL: {public_url}")

#import threading

#def run_app():
 #   !streamlit run app.py --server.port 8501 --server.enableCORS false --server.enableXsrfProtection false --clear-cache &
!pip freeze > requirements.txt

# Start ngrok tunnel
#public_url = ngrok.connect(8501)
#print(f"Public URL: {public_url}")

# Run the app
#thread = threading.Thread(target=run_app, args=())
#thread.start()
!cat requirements.txt

from google.colab import files
files.download('requirements.txt')