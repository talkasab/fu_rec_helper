mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[theme]\n\
base=\"dark\"\n\
primaryColor=\"#4b8bff\"\n\
\n" > ~/.streamlit/config.toml
