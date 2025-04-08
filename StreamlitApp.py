{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import streamlit as st\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-08 14:14:41.647 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:41.681 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:42.087 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:42.088 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:42.089 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:42.090 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:42.092 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:42.093 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:42.094 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:42.095 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:42.096 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:42.096 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:42.098 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:42.099 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:42.104 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:42.105 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:42.107 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:42.108 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "/var/folders/s5/w23ysbrd4mb00w78_80t58tm0000gn/T/ipykernel_21790/3929491848.py:23: UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown\n",
      "  plt.show()\n",
      "2025-04-08 14:14:42.218 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:42.648 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-04-08 14:14:42.657 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "st.title('My Name App')\n",
    "\n",
    "# reading in the data\n",
    "url = 'https://raw.githubusercontent.com/esnt/Data/refs/heads/main/Names/popular_names.csv'\n",
    "names = pd.read_csv(url)\n",
    "\n",
    "names = names.rename(columns={'n':'count'})\n",
    "\n",
    "# pick a name\n",
    "noi = st.text_input('Enter a name') # name of interest\n",
    "#soi = st.radio('Choose the sex to plot', ['M','F']) # sex of interest\n",
    "plot_female = st.checkbox('Plot female line')\n",
    "plot_male = st.checkbox('Plot male line')\n",
    "name_df = names[names['name']==noi]\n",
    "\n",
    "# create plot\n",
    "fig = plt.figure(figsize=(10,5))\n",
    "sns.lineplot(x=name_df['year'], y=name_df['count'], hue=name_df['sex'])\n",
    "plt.title(f'Plot of {noi}')\n",
    "plt.xlabel('year')\n",
    "plt.ylabel('count')\n",
    "plt.xticks(rotation=45)\n",
    "plt.show()\n",
    "\n",
    "st.pyplot(fig)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "env386",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
