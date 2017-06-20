set -e
module load gcc/4.9.0
#
echo "Processing fort.1111 = < T >"
touch mean sig t0
for i in {1..129}; do awk -v i=$i '{ print $i}' fort.1111 | /home/r4/flageul/dns_iztok/ar/arsel --subtract-mean > tmp; more tmp | head -n8 | tail -n1 | cut -c12- >> mean; more tmp | head -n9 | tail -n1 | cut -c12- >> sig; more tmp | head -n15 | tail -n1 | cut -c12- >> t0; done
paste yy mean sig t0 > tmean
rm mean sig t0
#
echo "Processing fort.1112 = < T' ** 2 >"
touch mean sig t0
for i in {1..129}; do awk -v i=$i '{ print $i}' fort.1112 | /home/r4/flageul/dns_iztok/ar/arsel --subtract-mean > tmp; more tmp | head -n8 | tail -n1 | cut -c12- >> mean; more tmp | head -n9 | tail -n1 | cut -c12- >> sig; more tmp | head -n15 | tail -n1 | cut -c12- >> t0; done
paste yy mean sig t0 > tvariance
rm mean sig t0
#
echo "Processing fort.1114 = < T' ** 4 >"
touch mean sig t0
for i in {1..129}; do awk -v i=$i '{ print $i}' fort.1114 | /home/r4/flageul/dns_iztok/ar/arsel --subtract-mean > tmp; more tmp | head -n8 | tail -n1 | cut -c12- >> mean; more tmp | head -n9 | tail -n1 | cut -c12- >> sig; more tmp | head -n15 | tail -n1 | cut -c12- >> t0; done
paste yy mean sig t0 > t4th-moment
rm mean sig t0
#
echo "Processing fort.1116 = < Tdiss >"
touch mean sig t0
for i in {1..129}; do awk -v i=$i '{ print $i}' fort.1116 | /home/r4/flageul/dns_iztok/ar/arsel --subtract-mean > tmp; more tmp | head -n8 | tail -n1 | cut -c12- >> mean; more tmp | head -n9 | tail -n1 | cut -c12- >> sig; more tmp | head -n15 | tail -n1 | cut -c12- >> t0; done
paste yy mean sig t0 > tdiss
rm mean sig t0
#
echo "Processing fort.1118 = < Tdiss ** 2 >"
touch mean sig t0
for i in {1..129}; do awk -v i=$i '{ print $i}' fort.1118 | /home/r4/flageul/dns_iztok/ar/arsel --subtract-mean > tmp; more tmp | head -n8 | tail -n1 | cut -c12- >> mean; more tmp | head -n9 | tail -n1 | cut -c12- >> sig; more tmp | head -n15 | tail -n1 | cut -c12- >> t0; done
paste yy mean sig t0 > tdissvariance
rm mean sig t0
#
echo "Done, terminus."
