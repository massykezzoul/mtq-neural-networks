import os.path

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam

class MTQModel():
    model_name = None
    model = None 
    
    def __init__(self, model_name=None):
        self.model_name = model_name

    def build_dense(self, input_shape, n_neurons=[32,64,2],learning_rate=0.0001, load=True, summary=False):
        if load and (self.model_name == None or not os.path.isdir(self.model_name)):
            raise ValueError("Can't load file in: "+self.model_name)

        if load:
            self.model = keras.models.load_model(self.model_name)
        else:
            # Creating the model
            self.model = Sequential([Dense(n_neurons[0], input_shape=input_shape, activation='relu')] +
                [Dense(n, activation='relu') for n in n_neurons[1:-1]] +            
                [Dense(n_neurons[-1], activation='softmax')]
            )
            self.model.compile(optimizer=Adam(learning_rate=learning_rate), loss='mean_squared_error', metrics=['accuracy'])

            if summary:
                self.model.summary()
            
    def fit(self, x, y, batch_size=12, epochs=15, verbose=2, save=True):
        self.model.fit(x=x, y=y,batch_size=batch_size, epochs=epochs, verbose=verbose)
        if save:
            self.model.save(self.model_name)

    def get_model(self):
        return self.model

    def get_hidden_layers_outputs(self, x_train):
        hidden_layers = [h_layer.output for h_layer in self.model.layers[:-1]]

        return keras.Model(inputs=self.model.inputs,
                                outputs=hidden_layers)(x_train)
