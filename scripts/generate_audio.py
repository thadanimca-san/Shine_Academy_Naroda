import os
from gtts import gTTS

def main():
    audio_dir = "assets/audio"
    os.makedirs(audio_dir, exist_ok=True)
    
    variants = [
        {
            "filename": "ye_to_mast_hai_1.mp3",
            "text_hi": "यह तो मस्त है, शाइन अकादमी नरोडा से सीखना ही पड़ेगा!"
        },
        {
            "filename": "ye_to_mast_hai_2.mp3",
            "text_hi": "यह तो मस्त मस्त है, शाइन अकादमी से इसको तो और ज्यादा सीखना पड़ेगा!"
        },
        {
            "filename": "ye_to_mast_hai_3.mp3",
            "text_hi": "यह तो जोरदार है, शाइन अकादमी नरोडा से इसी तरह सीखता रहना पड़ेगा!"
        },
        {
            "filename": "ye_to_mast_hai_4.mp3",
            "text_hi": "क्या बात है! यह तो एकदम मस्त है, शाइन अकादमी से सीखना ही पड़ेगा!"
        },
        {
            "filename": "ye_to_mast_hai_5.mp3",
            "text_hi": "बहुत खूब! यह मस्त है, शाइन अकादमी नरोडा से सीखना ही पड़ेगा।"
        },
        {
            "filename": "ye_to_mast_hai_6.mp3",
            "text_hi": "यह तो बिल्कुल मस्त है। शाइन अकादमी से ऐसे ही सीखना पड़ेगा।"
        },
        {
            "filename": "ye_to_mast_hai_7.mp3",
            "text_hi": "यह बहुत बढ़िया है। शाइन अकादमी नरोडा से हमेशा सीखना पड़ेगा।"
        },
        {
            "filename": "ye_to_mast_hai_8.mp3",
            "text_hi": "यह तो एकदम गोल्ड है! शाइन अकादमी से सीखना तो पड़ेगा ही।"
        }
    ]

    for variant in variants:
        try:
            tts = gTTS(text=variant["text_hi"], lang='hi')
            tts.save(os.path.join(audio_dir, variant["filename"]))
            print(f"Generated {variant['filename']}")
        except Exception as e:
            print(f"Error generating {variant['filename']}:", e)

if __name__ == "__main__":
    main()
