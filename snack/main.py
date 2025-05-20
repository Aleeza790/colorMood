import streamlit as st
import random

# Class to handle color moods and quotes
class ColorMood:
    def __init__(self, color: str, quotes: list[str], color_hex: str):
        self.color = color.lower()
        self.quotes = quotes
        self.color_hex = color_hex

    def get_random_quote(self):
        return random.choice(self.quotes)

# Manager class to handle different colors and their quotes
class ColorQuoteManager:
    def __init__(self):
        self.color_moods = {}
        self._load_colors()

    def _load_colors(self):
        self.color_moods = {
            "red": ColorMood("Red", [
                "❤️ Red symbolizes passion and energy!",
                "🔥 Feeling bold? That’s the power of Red!",
                "🚗 Red sparks excitement and action."
            ], "#FF5733"),
            "blue": ColorMood("Blue", [
                "💙 Blue brings calm and serenity.",
                "🌊 Feeling peaceful? That’s the magic of Blue.",
                "🔷 Blue inspires trust and wisdom."
            ], "#3498DB"),
            "green": ColorMood("Green", [
                "💚 Green means growth and harmony.",
                "🌿 Feeling balanced? Thank Green for that!",
                "🌱 Green symbolizes renewal and nature."
            ], "#2ECC71"),
            "yellow": ColorMood("Yellow", [
                "💛 Yellow shines with happiness and optimism.",
                "🌞 Feeling joyful? Yellow lights up your mood!",
                "✨ Yellow sparks creativity and energy."
            ], "#F1C40F"),
            "purple": ColorMood("Purple", [
                "💜 Purple represents luxury and wisdom.",
                "🎨 Feeling creative? Purple fuels imagination.",
                "🔮 Purple inspires mystery and magic."
            ], "#9B59B6"),
            "orange": ColorMood("Orange", [
                "🧡 Orange radiates enthusiasm and warmth.",
                "🍊 Feeling energetic? Orange boosts your spirit!",
                "🎉 Orange encourages social interaction and fun."
            ], "#FF7F50"),
            "pink": ColorMood("Pink", [
                "💗 Pink conveys love and kindness.",
                "🌸 Feeling gentle? Pink nurtures your soul.",
                "🤗 Pink symbolizes compassion and care."
            ], "#FF69B4")
        }

    def get_quote_by_color(self, color: str):
        return self.color_moods.get(color.lower()).get_random_quote()

    def available_colors(self):
        return list(self.color_moods.keys())

    def get_display_color_options(self):
        emoji_map = {
            "red": "❤️ Red",
            "blue": "💙 Blue",
            "green": "💚 Green",
            "yellow": "💛 Yellow",
            "purple": "💜 Purple",
            "orange": "🧡 Orange",
            "pink": "💗 Pink"
        }
        return [emoji_map[color] for color in self.available_colors()]

    def get_color_from_display(self, display_color: str):
        return display_color.split(" ")[1].lower()

# Main Streamlit application
def main():
    st.set_page_config(page_title="ColorMood Quotes", page_icon="🎨")

    # Header with custom styling
    st.markdown("<h1 style='color:#6C63FF;'>🎨 ColorMood - Pick a Color, Get a Quote</h1>", unsafe_allow_html=True)
    st.write("Select your favorite color and receive a mood-boosting quote!")

    manager = ColorQuoteManager()

    # Display color options with a color swatch
    display_colors = manager.get_display_color_options()
    selected_display_color = st.selectbox("Choose a color:", options=display_colors)

    # Get the corresponding color code from display
    selected_color = manager.get_color_from_display(selected_display_color)
    selected_color_hex = manager.color_moods[selected_color].color_hex

    # Set background color based on selected color
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {selected_color_hex};
            color: white;
        }}
        </style>
        """, unsafe_allow_html=True)

    # Button to fetch quote
    if st.button("✨ Get My Quote"):
        quote = manager.get_quote_by_color(selected_color)
        if quote:
            st.success(quote)
        else:
            st.error("Oops! Couldn't find a quote for that color.")

    # Option to like or save the quote
    if st.button("👍 Like this quote"):
        st.write("Thank you for liking the quote!")

if __name__ == "__main__":
    main()

