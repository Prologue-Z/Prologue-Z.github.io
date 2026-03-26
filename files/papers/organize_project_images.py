import os
import shutil

# 项目图片映射
projects = {
    'almd-control': {
        'source_dir': 'extracted_images_2024',
        'figures': {
            '01_robot_modeling': 'page2_fig1.png',  # Fig. 1 - 机器人建模
            '02_parameter_estimation': 'page4_fig1.png',  # Fig. 2 - 参数估计
            '03_fitness_evolution': 'page5_fig2.png',  # Fig. 3 - 适应度进化
            '04_experiment_comparison': 'page5_fig1.png',  # Fig. 4 - 实验对比
            '05_error_analysis': 'page6_fig1.png',  # Fig. 5 - 误差分析
            '06_parameter_changes': 'page7_fig1.png',  # Fig. 6 - 参数变化
            '07_data_acquisition': 'page8_fig1.png',  # Fig. 7 - 数据采集
            '08_mlp_comparison': 'page9_fig1.png',  # Fig. 9 - MLP 对比
            '09_control_results': 'page10_fig1.png',  # Fig. 10 - 控制结果
            '10_prototype': 'page11_fig1.png',  # Fig. 11 - 机器人原型
            '11_control_scheme': 'page11_fig2.png',  # Fig. 12 - 控制方案
            '12_final_results': 'page12_fig1.png',  # Fig. 13 - 最终结果
        }
    },
    'variable-gain': {
        'source_dir': 'extracted_images_2022',
        'figures': {
            '01_robot_design': 'page3_fig1.png',  # 机器人设计
            '02_control_scheme': 'page5_fig1.png',  # 控制方案
            '03_experiment_setup': 'page7_fig1.png',  # 实验装置
            '04_results': 'page8_fig1.png',  # 实验结果
        }
    },
    'cyclotomic-model': {
        'source_dir': 'extracted_images_2025_cyclotomic',
        'figures': {
            '01_kinematic_model': 'page2_fig1.jpeg',  # 运动学模型
            '02_robot_design': 'page3_fig1.jpeg',  # 机器人设计
            '03_experiments': 'page4_fig1.png',  # 实验
        }
    },
    'dual-rotational-dofs': {
        'source_dir': 'extracted_images_2025_dual_rotation',
        'figures': {
            '01_robot_design': 'page2_fig1.jpeg',  # 机器人设计
            '02_mechanism': 'page4_fig1.png',  # 机构
            '03_experiments': 'page5_fig1.jpeg',  # 实验
        }
    }
}

base_path = '/home/admin/.openclaw/workspace/projects/个人主页/source/images/projects'

for project_name, config in projects.items():
    project_dir = os.path.join(base_path, project_name)
    os.makedirs(project_dir, exist_ok=True)
    
    source_dir = os.path.join('/home/admin/.openclaw/workspace/projects/个人主页/source/files/papers', config['source_dir'])
    
    print(f"\n处理项目：{project_name}")
    print(f"源目录：{source_dir}")
    
    for fig_name, fig_file in config['figures'].items():
        src_path = os.path.join(source_dir, fig_file)
        dst_path = os.path.join(project_dir, f"{fig_name}.png" if fig_file.endswith('.jpeg') else fig_file)
        
        if os.path.exists(src_path):
            shutil.copy2(src_path, dst_path)
            print(f"  ✅ {fig_file} -> {fig_name}")
        else:
            print(f"  ❌ 未找到：{fig_file}")

print("\n🎉 图片整理完成！")
