import open3d as o3d
import threading

def visualize_point_cloud(file_path):
    def visualize():
        # Load point cloud
        pcd = o3d.io.read_point_cloud(file_path)

        # Visualize the point cloud in a non-blocking way
        vis = o3d.visualization.Visualizer()
        vis.create_window()
        vis.add_geometry(pcd)
        vis.poll_events()
        vis.update_renderer()

        # Keep the window open
        vis.run()
        vis.destroy_window()

    # Run the visualization in a separate thread
    threading.Thread(target=visualize).start()

# Example usage
if __name__ == "__main__":
    file_path = "bunny.ply"
    visualize_point_cloud(file_path)
    print("Point cloud visualized successfully! The visualization window will remain open.")