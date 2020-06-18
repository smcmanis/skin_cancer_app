from tensorflow import keras, device


# with device('/cpu:0'):
#     model = keras.models.load_model('/home/simon/projects/uni/dlcnn_autumn20/a3/skin_cancer/model/inception_savedmodel_v2')

def predict(img):
    # Using CPU because GPU causing errors on my laptop
    with device('/cpu:0'):
        model = keras.models.load_model('/home/simon/projects/uni/dlcnn_autumn20/a3/skin_cancer/model/inception_savedmodel_v2')
        return model.predict(img)