#Port Discovery
#             *     ,MMM8&&&.            *
#                  MMMM88&&&&&    .
#                 MMMM88&&&&&&&
#     *           MMM88&&&&&&&&
#                 MMM88&&&&&&&&
#                 'MMM88&&&&&&'
#                   'MMM8&&&'      *
#          |\___/|
#          )     (             .              '
#         =\     /=
#           )===(       *
#          /     \
#          |     |
#         /       \
#         \       /
#  _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
#  |  |  |  |( (  |  |  |  |  |  |  |  |  |  |
#  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
#  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
#  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
#     |  |  |  |  |  |  |  |  |  |  |  |  |  |
#!/bin/bash

function ctrl_c(){
    echo -e "\n\n[!] Quit\n"
    tput cnorm; exit 1
}

#ctrl+C
trap ctrl_c INT

tput civis

for port in $(seq 1 65535); do
    timeout 1 bash -c "echo '' > /dev/tcp/INSERT-IP-HERE/$port" 2>/dev/null && echo "Port $port - Open" &
done; wait

tput cnorm
