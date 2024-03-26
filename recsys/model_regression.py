import os
import pandas as pd
from tensorflow.keras.layers import (
    Input,
    IntegerLookup,
    Embedding,
    Flatten,
    Dot,
    Concatenate,
    Dense,
)
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

DATA_DIR = os.path.join(os.path.dirname(__file__), "local")
TRAIN_PATH = f"{DATA_DIR}/train.csv"
TEST_PATH = f"{DATA_DIR}/test.csv"
MODEL_PATH = f"{DATA_DIR}/model.h5"

# Load the MovieLens dataset (you can replace it with your own data)
# Assuming you have a CSV file with columns: 'user_id', 'movie_id', 'rating'
train = pd.read_csv(TRAIN_PATH)
test = pd.read_csv(TEST_PATH)

# Unique users and movies
all_users = train["user_id"].unique()
all_movies = train["movie_id"].unique()

# Create user and movie input layers
user_input = Input(shape=(1,), name="user_input")
movie_input = Input(shape=(1,), name="movie_input")

# Create user and movie IntegerLookup
user_as_integer = IntegerLookup(vocabulary=all_users)(user_input)
movie_as_integer = IntegerLookup(vocabulary=all_movies)(movie_input)

# Create user and movie embeddings
user_embedding = Embedding(input_dim=len(all_users) + 1, output_dim=32)(user_as_integer)
movie_embedding = Embedding(input_dim=len(all_movies) + 1, output_dim=32)(
    movie_as_integer
)

# Model1: dot product of user and movie embeddings
# dot_product = Dot(axes=2)([user_embedding, movie_embedding])
# flatten = Flatten()(dot_product)

# Model2: dense product of user and movie embeddings
concatted = Concatenate(axis=2)([user_embedding, movie_embedding])
dense1 = Dense(32, activation='relu')(concatted)
dense2 = Dense(1, activation='linear')(dense1)
flatten = Flatten()(dense2)

# Build and compile the model
model = Model(inputs=[user_input, movie_input], outputs=flatten)
model.compile(loss="mean_squared_error", optimizer="adam")

# Train the model
early_stop = EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True)
checkpoint = ModelCheckpoint(MODEL_PATH, monitor="val_loss", save_best_only=True)
model.fit(
    [train["user_id"], train["movie_id"]],
    train["user_rating"],
    epochs=10,
    batch_size=64,
    validation_split=0.2,
    callbacks=[early_stop, checkpoint],
)

# Evaluate the model
loss = model.evaluate([test["user_id"], test["movie_id"]], test["user_rating"])
print(f"Test Loss: {loss}")