import os
from Bio import SeqIO

# 1. Klasördeki tüm .fasta dosyalarını listele
fasta_files = [f for f in os.listdir() if f.endswith(".fasta")]

if not fasta_files:
    print("Klasörde .fasta dosyası bulunamadı!")
else:
    print(f"Bulunan dosyalar: {fasta_files}")

    for fasta in fasta_files:
        print(f"\nİşleniyor: {fasta}")
        
        # 2. FASTA dosyasını oku
        records = list(SeqIO.parse(fasta, "fasta"))
        
        if records:
            # Ödev gereği: Tanımlayıcıları (ID) ekrana yazdır
            for record in records:
                print(f"Sequence ID: {record.id}")
                
                # GenBank formatı için molekül tipi şarttır
                if "molecule_type" not in record.annotations:
                    record.annotations["molecule_type"] = "protein"

            # 3. Çıktı dosya adını belirle
            output_file = fasta.replace(".fasta", ".gb")

            # 4. Dosyayı güvenli bir şekilde kaydet (0 byte hatasını önler)
            try:
                with open(output_file, "w") as output_handle:
                    SeqIO.write(records, output_handle, "genbank")
                print(f"Başarıyla kaydedildi: {output_file}")
            except Exception as e:
                print(f"Dönüştürme hatası: {e}")
        else:
            print(f"Uyarı: {fasta} dosyası boş!")

print("\n--- Tüm işlemler tamamlandı. ---")
