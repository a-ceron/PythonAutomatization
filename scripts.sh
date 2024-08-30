# Prtición para enviar un mensaje
curl -i -X POST `
  https://graph.facebook.com/v20.0/371073332759638/messages `
  -H 'Authorization: Bearer EAAfYo27wulsBOx2bjgmjAZBqIQO1Pq3P171wZCzhVdKZBEJyOIYUrPEFSBfHFAtOXmWqwSZANxl22j8qWg4kZBlf01UhVDqfFmZCnC9k1JZBDlJtcZBDXl3dNolY5HSz6cobdPVQoUOX23OwR7wOZBZB60hTBvL4BoeqZAPUODKP8A80jJz5mouQEtFUNS1qWBYXbZBETZAvGBBTColmHgUZAEBGJTBdw4oz4ZD' `
  -H 'Content-Type: application/json' `
  -d '{ \"messaging_product\": \"whatsapp\", \"to\": \"525562112408\", \"type\": \"template\", \"template\": { \"name\": \"hello_world\", \"language\": { \"code\": \"en_US\" } } }'

# TOken temporal
  curl -X GET "https://graph.facebook.com/oauth/access_token
  ?client_id=2208521289513563
  &client_secret=3389186c9a7b7ef1840ba7d0c06d90bf 
  &grant_type=client_credentials"

# Información del negocio
curl -i -X GET 'https://graph.facebook.com/v20.0/2208521289513563' \
  -H 'Authorization: Bearer 2208521289513563|c9UO8hhwHU3DOEeCE5Qa2Xhhhg4'

# Informacion de los contactos
curl -X GET "https://graph.facebook.com/v20.0/2208521289513563/phone_numbers
      ?access_token=2208521289513563|c9UO8hhwHU3DOEeCE5Qa2Xhhhg4"