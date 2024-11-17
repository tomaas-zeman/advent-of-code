year=$1
day=$2
lang=$3

if [[ -z "$year" ]] || [[ -z "$day" ]] || [[ -z "$lang" ]]; then
    echo "Usage:"
    echo "./new_day.sh <year> <day> <lang: ts|py>"
    echo "./new_day.sh 2024 01 ts"
    exit 1
fi

mkdir -p year${year}/day${day}
cp day_template_${lang}/* year${year}/day${day}
