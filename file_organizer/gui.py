import streamlit as st
import os
from main import organize_files

st.set_page_config(page_title="📂 Smart File Organizer", layout="centered")

st.title("📂 Smart File Organizer")
st.write("Organize all your files into categories automatically using keyword rules!")

# Default folder path suggestion
default_path = os.path.join(os.path.expanduser("~"), "Documents")

# Input for folder path
folder_path = st.text_input("Enter the full folder path to organize:", default_path)

if st.button("🚀 Organize Folder"):
    if folder_path and os.path.exists(folder_path):
        with st.spinner("Organizing files..."):
            results = organize_files(folder_path)

        st.success(f"✅ Folder '{folder_path}' organized successfully!")

        st.subheader("📊 Summary")
        st.write(f"**Moved Files:** {len(results['moved'])}")
        st.write(f"**Duplicates Skipped:** {len(results['duplicates'])}")
        st.write(f"**Failed Moves:** {len(results['failed'])}")

        if results["moved"]:
            st.write("### ✅ Organized Files")
            for f, cat in results["moved"]:
                st.write(f"- {f} → {cat}")

        if results["duplicates"]:
            st.write("### ⏩ Duplicates")
            for f in results["duplicates"]:
                st.write(f"- {f}")

        if results["failed"]:
            st.write("### ⚠️ Failed Files")
            for f, err in results["failed"]:
                st.write(f"- {f}: {err}")
    else:
        st.error("❌ Please enter a valid folder path!")
