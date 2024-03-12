import streamlit as st
import pydeck as pdk
import time

# Initial radius of the circle
radius = 100  # This is in meters

# Center of the map and circle (latitude, longitude)
center = [37.76, -122.4]  # Example: San Francisco

# Configure the PyDeck view
view_state = pdk.ViewState(latitude=center[0], longitude=center[1], zoom=11)

# Function to create a PyDeck layer for a circle with a specific radius
def create_circle_layer(radius):
    return pdk.Layer(
        "ScatterplotLayer",
        data=[{"position": center}],
        get_position="position",
        get_radius=radius,
        get_fill_color=[255, 0, 0, 140],  # RGBA color
        get_line_color=[0, 0, 0, 0],
        pickable=True,
        opacity=0.8,
    )

# Streamlit app main loop
st.title("Growing Circle Animation on a Map")

# Loop to update the circle size and redraw the map
for _ in range(10):  # Update 10 times
    # Create the PyDeck layer with the current radius
    circle_layer = create_circle_layer(radius)
    
    # Create the PyDeck map with the circle
    deck = pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=view_state,
        layers=[circle_layer],
    )
    
    # Display the map in the Streamlit app
    st.pydeck_chart(deck)
    
    # Increase the radius for the next iteration
    radius += 100  # Increase by 100 meters each time
    
    # Pause to see the animation effect
    time.sleep(1)
