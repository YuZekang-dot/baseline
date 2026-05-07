#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
###########################################################################
# Copyright © 1998 - 2026 Tencent. All Rights Reserved.
###########################################################################
"""
Author: Tencent AI Arena Authors

PPO hyperparameters and model configuration for Drone Obstacle Navigation.
无人机避障导航 PPO 超参数及模型配置。
"""


class Config:
    # ========== Fixed Task Dimensions / 固定任务维度 ==========
    TASK_NAME = "ObstacleHover"
    OBS_DIM = 95
    ACTION_DIM = 4
    MAX_WAYPOINTS = 8
    OBSTACLE_FEATURE_DIM = 32
    TIME_ENCODING_DIM = 4

    # ========== Training Hyperparameters / 训练超参数 ==========
    LEARNING_RATE = 0.0005
    CLIP_PARAM = 0.1
    GAMMA = 0.995
    LAM = 0.95
    VALUE_LOSS_COEF = 0.5
    ENTROPY_COEF = 0.001
    MAX_GRAD_NORM = 10.0

    # ========== Training Schedule / 训练调度 ==========
    NUM_LEARNING_EPOCHS = 4
    NUM_MINI_BATCHES = 16
    NUM_STEPS_PER_ENV = 64

    # ========== Model Architecture / 模型结构 ==========
    ACTOR_HIDDEN_DIMS = [256, 128, 64]
    CRITIC_HIDDEN_DIMS = [256, 128, 64]
    ACTIVATION = "elu"
    INIT_NOISE_STD = 1.0
    FIXED_STD = False

    # ========== Reward Coefficients / 奖励系数 ==========
    REWARD_DISTANCE_SCALE = 0.6
    DISTANCE_REWARD_MULTIPLIER = 6.0
    GOAL_REACHED_REWARD = 100.0
    IN_ARENA_REWARD = 0.0
    OUT_OF_ARENA_PENALTY = 100.0
