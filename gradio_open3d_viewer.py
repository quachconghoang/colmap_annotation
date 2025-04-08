import gradio as gr
import open3d as o3d
import numpy as np

def visualize_point_cloud(file):
    # Load point cloud
    pcd = o3d.io.read_point_cloud(file.name)
    
    # Visualize the point cloud
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(pcd)
    vis.run()
    vis.destroy_window()

    return "Point cloud visualized successfully!"

iface = gr.Interface(
    fn=visualize_point_cloud,
    inputs=gr.components.File(label="bunny.ply"),
    outputs=gr.components.Textbox(),
    title="Open3D Point Cloud Viewer",
    description="Upload a point cloud file to visualize it using Open3D."
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860, share=True)