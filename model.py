import numpy as np
import librosa
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from sklearn.preprocessing import LabelEncoder
import sys
from pydub import AudioSegment

# MFCC özelliklerini çıkarmak için fonksiyon
def feature_extractor(file):
    audio, sample_rate = librosa.load(file, res_type="scipy")
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_scaled_features = np.mean(mfccs_features.T, axis=0)
    return mfccs_scaled_features

# Model mimarisini oluşturma
def create_model(input_shape, num_labels):
    model = Sequential()
    model.add(Dense(125, input_shape=(input_shape,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    model.add(Dense(250))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    model.add(Dense(250))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    model.add(Dense(250))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    model.add(Dense(125))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    model.add(Dense(num_labels))
    model.add(Activation('softmax'))

    return model

# Model ağırlıklarını yükleme
model = create_model(input_shape=40, num_labels=20)  # 'num_labels' verisetinize göre ayarlayın
model.load_weights('weights.h5')

# Modeli derleme (eğitimde kullanılan aynı yapılandırma ile)
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

# Ses dosyasını wav formatına dönüştürme fonksiyonu
def convert_to_wav(file_path):
    audio = AudioSegment.from_file(file_path)
    wav_path = file_path.replace(file_path.split('.')[-1], 'wav')
    audio.export(wav_path, format='wav')
    return wav_path

# Konuşmacıyı tahmin etme fonksiyonu
def predict_speaker(file_path):
    mfccs_features = feature_extractor(file_path)
    mfccs_features = np.expand_dims(mfccs_features, axis=0)

    # Model tahmini
    predicted_label = model.predict(mfccs_features)

    # Tahmin edilen etiketi orijinal etikete dönüştürme
    your_labels = ["aew", "ahw", "aup", "awb", "axb", "bdl", "clb", "eey", "emr", "fem", "gka", "jmk", "ksp", "ljm", "lnh", "rms", "rxr", "sel", "slp", "slt"]
    labelencoder = LabelEncoder()
    labelencoder.fit(your_labels)

    # Olasılık eşik değeri
    threshold = 0.5
    # En yüksek olasılığı ve indeksini bulun
    max_prob = np.max(predicted_label[0])
    result = np.argmax(predicted_label[0])

    # Eşik değeri ile karşılaştırın ve sonucu belirleyin
    if (max_prob < threshold):
        result_label = "other"

    elif(your_labels[result]!="emr" and your_labels[result]!="sel"):
        result_label = "other"
    else:
        result_label = your_labels[result]

    # Sınıf olasılıklarını yazdır
    probabilities = {your_labels[i]: float(prob) for i, prob in enumerate(predicted_label[0])}

    return result_label, probabilities

# Ana fonksiyon sadece doğrudan çağrıldığında çalıştırılır
if __name__ == "__main__":
    file_path = sys.argv[1]  # Komut satırından dosya yolu al
    wav_file_path = convert_to_wav(file_path)
    result_label, probabilities = predict_speaker(wav_file_path)
