import pprint
import pandas as pd
import xmldataset
from sqlalchemy.types import VARCHAR
from sqlalchemy import create_engine

ppsetup = pprint.PrettyPrinter(indent=4)
pp = ppsetup.pprint
xml_data = open('symdev1917.xml').read()

profile = """
    SymCLI_ML
        Symmetrix
            Symm_Info
                symid = dataset:mydata
            Device
                Dev_Info
                    pd_name = dataset:mydata
                    dev_name = dataset:mydata
                    configuration = dataset:mydata
                    device_group = dataset:mydata
                    number_of_raid_groups = dataset:mydata
                    encapsulated = dataset:mydata
                    encapsulated_wwn = dataset:mydata
                    encapsulated_array_id = dataset:mydata
                    encapsulated_device_name = dataset:mydata
                    attached_bcv = dataset:mydata
                    emulation = dataset:mydata
                    status = dataset:mydata
                    sa_status = dataset:mydata
                    user_pin = dataset:mydata
                    device_tag = dataset:mydata
                    snapvx_source = dataset:mydata
                    snapvx_target = dataset:mydata
                    dif1 = dataset:mydata
                    as400_gk = dataset:mydata
                    service_state = dataset:mydata
                    ssid = dataset:mydata
                    cache_partition_name = dataset:mydata
                    host_access_mode = dataset:mydata
                    extent_based_clone = dataset:mydata
                    host_cache_registered = dataset:mydata
                    optimized_read_miss = dataset:mydata
                    thin_pool_name = dataset:mydata
                    SRP_name = dataset:mydata
                Attached
                    BCV = dataset:mydata
                    VDEV = dataset:mydata
                Product
                    vendor = dataset:mydata
                    name = dataset:mydata
                    revision = dataset:mydata
                    serial_id = dataset:mydata
                    symid = dataset:mydata
                    wwn = dataset:mydata
                Label
                    type = dataset:mydata
                    defined_label = dataset:mydata
                Flags
                    ckd = dataset:mydata
                    worm_enabled = dataset:mydata
                    worm_protected = dataset:mydata
                    dynamic_spare_invoked = dataset:mydata
                    dynamic_rdf_capability = dataset:mydata
                    star_mode = dataset:mydata
                    star_recovery_capability = dataset:mydata
                    star_recovery_state = dataset:mydata
                    sqar_mode = dataset:mydata
                    radiant_managed = dataset:mydata
                    restricted_access_dev = dataset:mydata
                    rdb_checksum_enabled = dataset:mydata
                    non_exclusive_access = dataset:mydata
                    scsi3_persist_res = dataset:mydata
                    aclx = dataset:mydata
                    symmetrix_filesystem = dataset:mydata
                    snap_save_device = dataset:mydata
                    gatekeeper = dataset:mydata
                    datadev = dataset:mydata
                    meta = dataset:mydata
                    encap_dev_flag = dataset:mydata
                Capacity
                    block_size = dataset:mydata
                    cylinders = dataset:mydata
                    tracks = dataset:mydata
                    blocks = dataset:mydata
                    megabytes = dataset:mydata
                    kilobytes = dataset:mydata
                    gigabytes = dataset:mydata
                    terabytes = dataset:mydata
                    geometry_limited = dataset:mydata
                Device_External_Identity
                    wwn = dataset:mydata
                    device_geometry
                        geometry_type = dataset:mydata
                        sectors_per_tracks = dataset:mydata
                        tracks_per_cylinder = dataset:mydata
                        cylinders = dataset:mydata
                        blocks = dataset:mydata
                        megabytes = dataset:mydata
                        kilobytes = dataset:mydata
                        gigabytes = dataset:mydata
                        terabytes = dataset:mydata
                    Mirror_Set
                        Mirror
                            number = dataset:mydata
                            type = dataset:mydata
                            status = dataset:mydata
                            invalid_tracks = dataset:mydata
                            invalid_mbs = dataset:mydata
                            invalid_gbs = dataset:mydata
                            invalid_tbs = dataset:mydata
                    Back_End
                        Hyper
                            type = dataset:mydata
                            status = dataset:mydata
                            number = dataset:mydata
                            mirror_number = dataset:mydata
                            Disk
                                director = dataset:mydata
                                interface = dataset:mydata
                                tid = dataset:mydata
                                volume_number = dataset:mydata
                                spindle_id = dataset:mydata
                                disk_group = dataset:mydata
                                disk_group_name = dataset:mydata
                    RDF
                        RDF_Info
                            pair_state  = dataset:mydata
                            prevent_ra_online_upon_pwron  = dataset:mydata
                            suspend_state  = dataset:mydata
                            consistency_state  = dataset:mydata
                            consistency_exempt_state  = dataset:mydata
                            config_rdfa_wpace_exempt_state  = dataset:mydata
                            effective_rdfa_exempt_state  = dataset:mydata
                            WPace_Info
                                pacing_capable  = dataset:mydata
                                config_rdfa_wpace_exempt_state  = dataset:mydata
                                effective_rdfa_exempt_state
                                rdfa_wpace_state
                                rdfa_devpace_state
                            r1_invalids
                            r2_invalids
                            r2_larger_than_r1
                            paired_with_diskless
                            paired_with_concurrent
                            paired_with_cascaded
                            thick_thin_relationship
                            r2_not_ready_if_invalid
                            pair_configuration
                        Mode
                            mode
                            adaptive_copy
                            adaptive_copy_write_pending
                            adaptive_copy_skew
                            device_domino
                            star_mode
                            sqar_mode
                        Link
                            configuration
                            domino
                            prevent_automatic_recovery
                        Status
                            rdf
                            sa
                            ra
                            link
                            link_status_change_time
                        Local
                            dev_name







         """
output = xmldataset.parse_using_profile(xml_data, profile)
df = pd.DataFrame.from_records(output['mydata'],
                               columns=['symid', 'dev_name', 'configuration', 'device_group', 'ld_name', 'attached_bcv',
                                        'status', 'snapvx_source', 'snapvx_target', 'thin_pool_name', 'SRP_name',
                                        'vdev_tgt', 'wwn', 'snap_save_device', 'gatekeeper', 'meta', 'megabytes',
                                        'cylinders', 'blocks', 'kilobytes', 'pair_state', 'consistency_state', 'mode',
                                        'adaptive_copy', 'adaptive_copy_write_pending', 'link_status',
                                        'link_status_change_time', 'local_ra_group_num', 'remote_dev_name',
                                        'remote_symid', 'remote_wwn', 'remote_dev_state', 'filename'])
# df.drop_duplicates(subset='wwn', keep='first', inplace=True)


deleting_nan_values = df.apply(lambda x: pd.Series(x.dropna().values))
deleting_nan_values.drop_duplicates(subset='wwn', keep='first', inplace=True)

engine = create_engine('mysql://root:password@localhost/mysql')
with engine.connect() as conn, conn.begin():
    deleting_nan_values.to_sql('0298_symdev', conn, if_exists='replace', index=False)
