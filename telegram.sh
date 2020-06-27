#!/bin/bash

# Script by Valentin DEVILLE (https://github.com/MyTheValentinus/zabbix-telegram.sh/)

token="1326392960:AAFUiRYTRp_8iBu_vMqcvxnHox88LCxMrh8"
chat_id="-395670124"
TEXT="Mensagem enviada"
URL="https://api.telegram.org/bot${token}/sendMessage"
SUBJECT="teste"

MESSAGE=$(cat <<EOF
${SUBJECT}
${TEXT}
EOF
)

JSON=$(cat <<EOF
{
        "chat_id": "${chat_id}",
        "text": "${MESSAGE}",
        "parse_mode": "html",
        "disable_web_page_preview": True
}
EOF
)

curl -X POST -H "Content-Type: application/json" --data "${JSON}" $URL