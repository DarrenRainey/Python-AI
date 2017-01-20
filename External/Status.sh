# CPU USAGE
top -bn1 | grep "Cpu(s)" |            sed "s/.*, *\([0-9.]*\)%* id.*/\1/" |            awk '{print 100 - $1"% CPU USAGE"}'
# RAM USAGE
free | grep Mem | awk '{print $3/$2 * 100.0 "% RAM USAGE"}'
