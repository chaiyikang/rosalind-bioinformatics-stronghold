from newick import buildTree



def solution(tree):
    tree = buildTree(tree)
    names = []

    def preorderFindNames(tree):
        if tree.name is not None:
            names.append(tree.name)
        if not tree.children:
            return
        for child in tree.children:
            preorderFindNames(child)

    preorderFindNames(tree)
    names.sort()
    nameToIndex = {}
    for i, name in enumerate(names):
        nameToIndex[name] = i
    numberOfTaxa = len(names)

    def preorderMarkNames(tree, arr):
        if tree.name is not None:
            arr[nameToIndex[tree.name]] = 1
        if not tree.children:
            return
        for child in tree.children:
            preorderMarkNames(child, arr)


    def helper(tree):
        for child in tree.children:
            charArray = [0] * numberOfTaxa
            preorderMarkNames(child, charArray)
            if sum(charArray) > 1:
                print("".join([str(x) for x in charArray]))
        for child in tree.children:
            helper(child)

    helper(tree)


solution('''(((((((((((((((((Acanthosaura_galericulata,Pogona_cygnus),(Boa_falcinellus,Lobipes_coloratovillosum)),(Procellaria_novaeguineae,Teratolepis_cranwelli)),((Allobates_geniculata,Dahurinaia_ornata),Tringa_fissipes)),(((Bombus_undulata,Gonyosoma_parvus),(Lepus_not,Philacte_hendricksoni)),((Megaloperdix_caninus,Nemorhaedus_sudanensis),Ziphius_auratus))),((Canis_jaculus,Sus_medici),Python_spilota)),Pachytriton_weliczkowskii),(Cuon_paradoxus,Monticola_chrysargos)),Egretta_truncatus),Ceratophrys_albigula),Brachyramphus_arizonensis),(Bradypterus_aleutica,Notophthalmus_marmoratus)),Bombina_pusilla),Hemiscorpius_tarandus),Dyscophus_melonotis),(((((((Alloporus_acutus,Psammophis_exanthematicus),((((Basiliscus_penelope,Homalopsis_ferox),(Camptoloma_miliaris,Prunella_vertebralis)),((Crocodylus_hemionus,Haliaeetus_obsoleta),(Lycodon_varius,Scolopendra_cornix))),((Bufo_querquedula,Picus_naumanni),Nyroca_classicus))),Cyriopagopus_sujfunensis),Hadogenes_multituberculatus),Syrrhaptes_cristatellus),(((((Anthropoides_leporosum,(Bos_dorsalis,Uncia_montela)),((Elseya_lavaretus,Latastia_colchicus),Oligodon_rutila)),Ziphius_blythi),Aplopeltura_chukar),Prunella_moschiferus)),(Aythia_spaldingi,Perdix_cyanogaster))),Acanthosaura_septentrionalis,(((((((((((((((((((((Agama_quadrivirgata,Enhudra_monachus),((Bombina_stellio,(((Latastia_onocrotalus,Numenius_multifasciata),Pelusios_mirabilis),(Marmota_rostratus,Testudo_perrotetii))),Eutamias_japonensis)),(Cuon_milii,Dryobates_lesueurii)),((((((((((((((Almo_buccata,Chlidonias_eulophotes),Platalea_holbrooki),Mustela_clypeata),((((((((Anas_vermiculatus,Avicularia_diadema),((Calotes_salvator,((Lampropeltis_dexter,Sphenurus_tristis),Spizaetus_brevirostris)),Trionyx_lagopus)),(Salamandra_carinatus,Scaphiopus_unicolor)),((Platalea_adspersus,Python_geyri),Plethodon_communis)),(Oedura_maculatum,Tetraogallus_martensi)),(((((Buteo_cepediana,Corvus_regius),sibiricus_clypeata),Pelecanus_merganser),(((((Emydura_citrsola,Parabuthus_oedicnemus),Sphenops_pugnax),Tadorna_armata),Podoces_reticulatus),sibiricus_emilia)),Buthacus_fissipes)),(Pelodiscus_marmorata,Physignathus_bimaculata)),Glareola_caudata)),Canis_marmoratus),Cygnus_teniotis),((((((Bradyporus_boschas,((Chen_atriceps,(Mogera_constricticollis,(Paramesotriton_vulgaris,Vulpanser_microlepis))),(Coenobita_nigriceps,Equus_heliaca))),Upupa_spaldingi),Platalea_docilis),((Callipogon_nipalensis,Pusa_scripta),(Columba_bewickii,Mareca_undulata))),Lystrophis_leucophyllata),(((((Bradyporus_eremita,Gazella_conicus),Elaphe_stagnalis),Lutra_bairdii),Myotis_dentatus),Vanellus_vermiculatus))),Scolopax_leucophyllata),Basiliscus_cygnoides),Aplopeltura_gigas),(Ceratophrys_albirostris,Scolopax_nyroca)),(Apus_undulata,Chen_minutus)),Phelsuma_dactylisonans),Enhydris_opimus)),Tamias_naumanni),((Damon_nyroca,Monticola_nivalis),Telescopus_wogura)),((Agama_venulosa,Buthus_lutris),Epicrates_laevis)),(Megaptera_schrencki,Procellaria_leucorodia)),Argynnis_enydris),(Alectoris_spinifera,Rhabdophis_musicus)),(((Anthropoidae_laticauda,((((Bubulcus_salei,Gypaetus_fuscatus),Homopholis_leucopsis),Chondropython_brevipes),(Chlamydosaurus_nasicus,(Cynops_chukar,Varanus_stellatum)))),Kinosternon_wogura),((((Arenaria_pica,Trapelus_hispida),Bradypterus_colchicus),Latastia_lutra),Latastia_dennysii))),Leiurus_rapax),Geochelone_calamita),((Athene_papuana,Trachemys_tinnunculus),Siniperca_filipjevi)),Crocodylus_enydris),Eumeces_totanus),((Gonocephalus_himalayanus,Nyroca_ocellatus),Hysterocrates_Bernicla)),(Epipedobates_taezanowskyi,Rosalia_gobio)),(((((((((((Alauda_avinivi,Tetrao_tarda),Boa_helena),Numenius_lineatus),Asthenodipsas_occitanus),Paradoxornis_strepera),Porzana_garullus),Ptyodactylus_aureostriata),Circus_melonotis),Gazella_quinquestriatus),Ovis_cyanus),(Allobates_boa,Chelodina_galactonotus))),Chelodina_politus),(((((Bombus_peregrinus,Meles_squaterola),Phrynops_fissipes),(Nemachilus_grunniens,Pedostibes_himalayensis)),Emberiza_marmorata),Mesoplodon_caelebs)));''')
