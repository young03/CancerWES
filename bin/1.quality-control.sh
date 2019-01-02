### prepare dirs and scripts
mkdir script log
ln -s ~/users/wuyang/20181218-Cancer-WES-pipe/bin/ .

### prepare data files
python bin/output_cmd.py -f ~/data/20181218-TJZLYY-YJP-breastCancer-WES/data_info.txt -d ~/data/20181218-TJZLYY-YJP-breastCancer-WES/ -t rename -o dat >script/rename.sh
bash script/rename.sh   # link raw .fq.gz files to dat/

### run fastqc
mkdir fastqc_output
fastqc dat/*/*.fq.gz -o fastqc_output &>log/fastqc.log    # ls */*gz |xargs -I [] echo 'fastqc [] &' >fastqc.sh

### run multiqc
multiqc fastqc_output/ -o multiqc_output &>log/multiqc.log
