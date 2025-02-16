import streamlit as st
import pandas as pd

# Function to generate natural language descriptions
def generate_description(row):
    description = (
        f"The material is {row['material']} with a {row['structure']} crystal structure. "
        f"It has a composition of {row['composition']} and exhibits {row['twin_type']} nanotwinning. "
        f"The grain size is {row['grain_size']}, and the experiment was conducted at {row['temperature']}."
    )
    return description

# Streamlit app
def main():
    st.title("CSV to Natural Language Descriptions")
    st.write("Upload a CSV file to convert it into natural language descriptions.")

    # File upload
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)

        # Display the uploaded data
        st.write("### Uploaded Data")
        st.write(df)

        # Generate descriptions
        df["description"] = df.apply(generate_description, axis=1)

        # Display the generated descriptions
        st.write("### Generated Descriptions")
        st.write(df["description"])

        # Download the descriptions as a CSV file
        st.write("### Download Descriptions")
        output_csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download Descriptions as CSV",
            data=output_csv,
            file_name="nanotwin_descriptions.csv",
            mime="text/csv",
        )

# Run the app
if __name__ == "__main__":
    main()
