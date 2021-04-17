# Informations 

## Enable widgets with Jupyter Notebook

`jupyter nbextension enable --py widgetsnbextension`
`jupyter labextension install @jupyter-widgets/jupyterlab-manager`

## VBOX widgets with FigureWidgets

Ipywidgets (Vbox) not showing up on Jupyter notebook -> [solution](https://stackoverflow.com/questions/66371006/ipywidgets-vbox-not-showing-up-on-jupyter-notebook)

```shell
jupyter nbextension install --py plotlywidget --user
jupyter nbextension enable plotlywidget --user --py
```
