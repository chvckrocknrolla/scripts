#Host Discovery
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
        echo -e "\n\n[!] quitting.\n"
        tput cnorm; exit 1
}

#ctrl+C
trap ctrl_c INT

tput civis
for i in $(seq 1 254); do
        timeout 1 bash -c "ping -c 1 inserthereipnumber.$i" &>/dev/null && echo "[+] Host inserthereipnumber.$i - Active" &
done; wait
tput cnorm
