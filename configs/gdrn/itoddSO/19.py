_base_ = ["../../_base_/gdrn_base.py"]

OUTPUT_DIR = "output/gdrn/itoddSO/19/a"
INPUT = dict(
    DZI_PAD_SCALE=1.5,
    TRUNCATE_FG=True,
    CHANGE_BG_PROB=0.5,
    COLOR_AUG_PROB=0.8,
    MIN_SIZE_TRAIN=(960,),
    MAX_SIZE_TRAIN=1280,
    # MIN_SIZE_TRAIN_SAMPLING="choice",
    MIN_SIZE_TEST=960,
    MAX_SIZE_TEST=1280,
    COLOR_AUG_TYPE="code",
    COLOR_AUG_CODE=(
        "Sequential(["
        # Sometimes(0.5, PerspectiveTransform(0.05)),
        # Sometimes(0.5, CropAndPad(percent=(-0.05, 0.1))),
        # Sometimes(0.5, Affine(scale=(1.0, 1.2))),
        #"Sometimes(0.5, CoarseDropout( p=0.2, size_percent=0.05) ),"
        "Sometimes(0.5, GaussianBlur(1.2*np.random.rand())),"
        "Sometimes(0.5, Add((-25, 25), per_channel=0.3)),"
        "Sometimes(0.3, Invert(0.2, per_channel=True)),"
        "Sometimes(0.5, Multiply((0.6, 1.4), per_channel=0.5)),"
        "Sometimes(0.5, Multiply((0.6, 1.4))),"
        "Sometimes(0.5, LinearContrast((0.5, 2.2), per_channel=0.3))"
        "], random_order = False)"
        # aae
    ),
)

SOLVER = dict(
    IMS_PER_BATCH=24,
    TOTAL_EPOCHS=80,
    LR_SCHEDULER_NAME="flat_and_anneal",
    ANNEAL_METHOD="cosine",  # "cosine"
    ANNEAL_POINT=0.72,
    # REL_STEPS=(0.3125, 0.625, 0.9375),
    OPTIMIZER_CFG=dict(_delete_=True, type="Ranger", lr=1e-4, weight_decay=0),
    WEIGHT_DECAY=0.0,
    WARMUP_FACTOR=0.001,
    WARMUP_ITERS=1000,
)


DATASETS = dict(
    TRAIN=("itodd_pbr_19_train",),
    TEST=("itodd_pbr_19_test",),
    DET_FILES_TEST=(
        "datasets/BOP_DATASETS/itodd/test/test_bboxes/yolox_x_640_itodd_pbr_itodd_bop_test.json",),
    DET_TOPK_PER_OBJ=100,
    DET_THR=0.05,
)

DATALOADER = dict(
    # Number of data loading threads
    NUM_WORKERS=8,
    FILTER_VISIB_THR=0.3,
)

MODEL = dict(
    LOAD_DETS_TEST=True,
    PIXEL_MEAN=[0.0, 0.0, 0.0],
    PIXEL_STD=[255.0, 255.0, 255.0],
    CDPN=dict(
        ROT_HEAD=dict(
            FREEZE=False,
            ROT_CLASS_AWARE=False,
            MASK_CLASS_AWARE=False,
            XYZ_LW=1.0,
            REGION_CLASS_AWARE=False,
            NUM_REGIONS=32,
        ),
        PNP_NET=dict(
            R_ONLY=False,
            REGION_ATTENTION=True,
            MASK_ATTENTION="mul",
            WITH_2D_COORD=True,
            ROT_TYPE="allo_rot6d",
            TRANS_TYPE="centroid_z",
            PM_NORM_BY_EXTENT=True,
            PM_R_ONLY=True,
            CENTROID_LOSS_TYPE="L1",
            CENTROID_LW=1.0,
            Z_LOSS_TYPE="L1",
            Z_LW=1.0,
        ),
        TRANS_HEAD=dict(ENABLED=False),
    ),
)

VAL = dict(
    DATASET_NAME="itodd",
    SCRIPT_PATH="lib/pysixd/scripts/eval_pose_results_more.py",
    TARGETS_FILENAME="test_targets_bop19.json",
    ERROR_TYPES="mspd,mssd,vsd,ad,reS,teS",
    RENDERER_TYPE="cpp",  # cpp, python, egl
    SPLIT="test",
    SPLIT_TYPE="",
    N_TOP=-1,  # SISO: 1, VIVO: -1 (for LINEMOD, 1/-1 are the same)
    EVAL_CACHED=False,  # if the predicted poses have been saved
    SCORE_ONLY=False,  # if the errors have been calculated
    EVAL_PRINT_ONLY=False,  # if the scores/recalls have been saved
    EVAL_PRECISION=False,  # use precision or recall
    USE_BOP=True,  # whether to use bop toolkit
    
    SAVE_BOP_CSV_ONLY=True,
)


TEST = dict(EVAL_PERIOD=0, VIS=False, TEST_BBOX_TYPE="est")  # gt | est
