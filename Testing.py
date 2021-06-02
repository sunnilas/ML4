import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
sns.pairplot(tips)
plt.show()
st.balloons()
